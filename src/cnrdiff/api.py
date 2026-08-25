import re
import sqlite3
from contextlib import contextmanager
from enum import StrEnum
from pathlib import Path

import pandas as pd
from pyrtcm import RTCMReader

SQL_CREATE_TABLE_CNR = """
CREATE TABLE IF NOT EXISTS cnr (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    epoch INTEGER,
    satellite CHAR(3),
    tna CHAR(3),
    cnr REAL
);
"""

SQL_ADD_CNR = """
INSERT INTO cnr (epoch, satellite, tna, cnr)
VALUES (?, ?, ?, ?);
"""

SQL_GET_AVERAGE_CNR = """
SELECT
    satellite AS sat,
    tna,
    AVG(cnr) AS avg_cnr
FROM cnr
GROUP BY satellite, tna
ORDER BY satellite, tna;
"""

SQL_GET_AVERAGE_CNR_BY_SYS = """
SELECT
    SUBSTR(satellite, 1, 1) AS sys,
    tna,
    AVG(cnr) AS avg_cnr
FROM cnr
GROUP BY SUBSTR(satellite, 1, 1), tna
ORDER BY SUBSTR(satellite, 1, 1), tna;
"""


class FType(StrEnum):
    BNC_QC_LOG = "BNC_QC_LOG"
    RINEX3_OBS = "RINEX3_OBS"
    RTCM3_MSM4 = "RTCM3_MSM4"


SUFFIX_FTYPE_MAP = [
    (re.compile(r"..o", re.IGNORECASE), FType.RINEX3_OBS),
    (re.compile(r"obs", re.IGNORECASE), FType.RINEX3_OBS),
    (re.compile(r"rtcm", re.IGNORECASE), FType.RTCM3_MSM4),
    (re.compile(r"log", re.IGNORECASE), FType.BNC_QC_LOG),
]


def detect_ftype(fpath: Path) -> FType:
    """根据文件后缀识别观测数据文件类型

    依次与 SUFFIX_FTYPE_MAP 中的正则模式匹配，返回对应的文件类型枚举

    Parameters
    ----------
    fpath : Path
        观测数据文件路径

    Returns
    -------
    FType
        文件类型枚举

    Raises
    ------
    ValueError
        无法识别文件后缀时抛出
    """
    suffix = fpath.suffix.lstrip(".")
    for pattern, ftype in SUFFIX_FTYPE_MAP:
        if pattern.fullmatch(suffix):
            return ftype
    raise ValueError(f"Cannot detect file type from suffix: .{suffix}")


@contextmanager
def cnr_db(fpath: Path):
    """创建 CNR 数据库上下文，自动提交并关闭连接

    Yields
    ------
    tuple[sqlite3.Cursor, Path]
        数据库游标和 CNR 文件路径
    """
    cnr_path = fpath.with_suffix(".cnr")
    conn = sqlite3.connect(cnr_path)
    cursor = conn.cursor()
    cursor.execute(SQL_CREATE_TABLE_CNR)
    try:
        yield cursor, cnr_path
        conn.commit()
    finally:
        cursor.close()
        conn.close()


def bnc_qc_log_to_cnr(fpath: Path) -> Path:
    """Convert from BNC QC LOG

    将 BNC 质量检测日志文件转换为 CNR 格式

    Parameters
    ----------
    fpath : Path
        BNC QC LOG 文件路径

    Returns
    -------
    Path
        生成的 CNR 文件路径
    """
    with cnr_db(fpath) as (cursor, cnr_path), open(fpath, "r") as fstream:
        epoch = 0
        flag = 0
        for line in fstream:
            if flag != 0:
                data = line.split()
                sat = data[0]
                obsn = int(data[3]) // 2
                for i in range(obsn):
                    tna = "S" + data[4 + i * 6][1:3]
                    cnr = float(data[6 + i * 6])
                    cursor.execute(SQL_ADD_CNR, (epoch, sat, tna, cnr))
                flag -= 1
            if line.startswith(">"):
                epoch += 1
                flag = int(line[30:32])
    return cnr_path


def rinex3_obs_to_cnr(fpath: Path) -> Path:
    """Convert from RINEX3 OBS

    将 RINEX V3 观测文件转换为 CNR 格式

    Parameters
    ----------
    fpath : Path
        RINEX3 OBS 文件路径

    Returns
    -------
    Path
        生成的 CNR 文件路径

    References
    ----------
    1. https://files.igs.org/pub/data/format/rinex_4.00.pdf
    """
    with cnr_db(fpath) as (cursor, cnr_path), open(fpath, "r") as fstream:
        sys_tna = {}
        sys = " "
        for line in fstream:
            if "SYS / # / OBS TYPES" in line:
                tna = line[7:59].split()
                if line[0] != " ":
                    sys_tna[line[0]] = tna
                    sys = line[0]
                else:
                    sys_tna[sys] += tna
            elif "END OF HEADER" in line:
                break
        epoch = 0
        n_sat = 0
        for line in fstream:
            if n_sat != 0:
                sat = line[0:3]
                tna_val = [line[i : (i + 16)] for i in range(1, len(line), 16)]
                for i, tna in enumerate(sys_tna[line[0]]):
                    if tna.startswith("S"):
                        val = tna_val[i][10:16].replace(" ", "")
                        if val != "":
                            cnr = float(val)
                            cursor.execute(SQL_ADD_CNR, (epoch, sat, tna, cnr))
                n_sat -= 1
            if line.startswith(">"):
                epoch += 1
                n_sat = int(line[33:35])
    return cnr_path


def rtcm3_msm4_to_cnr(fpath: Path) -> Path:
    """Convert from RTCM3 MSM4

    用于转换 2017-01-01 以来一周之内的包含 MSM4 的 RTCM3 数据

    Parameters
    ----------
    fpath : Path
        RTCM3 文件路径

    Returns
    -------
    Path
        生成的 CNR 文件路径

    Notes
    -----
    请注意卫星 PRN 会转换为 RINEX3 定义的 snn 形式，其中，
    - 认定 QZSS 使用名义 PRN，即偏移量采用 192
    - SBAS 偏移量为 RINEX3 规定的 100，而不是 120
    - 其他卫星系统偏移量为 0

    References
    ----------
    1. https://software.rtcm-ntrip.org/wiki/NDF?version=4
    2. https://files.igs.org/pub/data/format/rinex_4.00.pdf
    3. https://github.com/tomojitakasu/RTKLIB/blob/master/src/rtcm3e.c
    """
    with cnr_db(fpath) as (cursor, cnr_path), open(fpath, "rb") as fstream:
        reader = RTCMReader(fstream, quitonerror=0)
        for _, msg in reader:
            if msg.ismsm:
                prn_offset = 0
                if msg.identity == "1074":
                    sys = "G"
                    gps_tow = msg.DF004
                elif msg.identity == "1084":
                    sys = "R"
                    glo_tow = msg.DF416 * 24 * 60 * 60 * 1000 + msg.DF034
                    # UTC has leaped 18 seconds since 2017-01-01
                    # TODO: optimize hard-coded 18s here
                    gps_tow = glo_tow - 3 * 60 * 60 * 1000 + 18 * 1000
                elif msg.identity == "1094":
                    sys = "E"
                    gps_tow = msg.DF248
                elif msg.identity == "1104":
                    sys = "S"
                    gps_tow = msg.DF004
                    prn_offset = 100
                elif msg.identity == "1114":
                    sys = "J"
                    gps_tow = msg.DF428
                    prn_offset = 192
                elif msg.identity == "1124":
                    sys = "C"
                    bds_tow = msg.DF427
                    # GPST - BDT = 14s
                    gps_tow = bds_tow + 14 * 1000
                elif msg.identity == "1134":
                    sys = "I"
                    gps_tow = msg.DF004

                for i in range(msg.NCell):
                    sig = getattr(msg, f"CELLSIG_{i + 1:02d}")
                    if sig == "/":
                        continue
                    tna = f"S{sig}"

                    prn = getattr(msg, f"CELLPRN_{i + 1:02d}")
                    prn = int(prn) - prn_offset
                    sat = f"{sys}{prn:02d}"

                    cnr = getattr(msg, f"DF403_{i + 1:02d}")
                    cursor.execute(SQL_ADD_CNR, (gps_tow, sat, tna, cnr))
    return cnr_path


def cnrconv(fpath: Path, ftype: FType) -> Path:
    """根据文件类型调用对应的转换函数

    Parameters
    ----------
    fpath : Path
        观测数据文件路径
    ftype : FType
        观测数据文件类型

    Returns
    -------
    Path
        生成的 CNR 文件路径
    """
    match ftype:
        case FType.BNC_QC_LOG:
            return bnc_qc_log_to_cnr(fpath)
        case FType.RINEX3_OBS:
            return rinex3_obs_to_cnr(fpath)
        case FType.RTCM3_MSM4:
            return rtcm3_msm4_to_cnr(fpath)


def cnrdiff(cnrs: list[Path], by_sys: bool = False) -> pd.DataFrame:
    """计算各测站相对于参考测站的载噪比差值

    第一个 CNR 文件为参考测站，返回参考站原始平均值和其余站差值

    Parameters
    ----------
    cnrs : list[Path]
        CNR 文件路径列表，第一个为参考测站
    by_sys : bool, optional
        为 True 时按卫星系统聚合，默认按卫星号

    Returns
    -------
    pd.DataFrame
        以卫星号（或卫星系统）和频点为 MultiIndex、测站名为列的差值表，
        参考站列为原始平均值，其余站列为相对参考站的差值
    """
    if by_sys:
        sql = SQL_GET_AVERAGE_CNR_BY_SYS
        key_col = "sys"
    else:
        sql = SQL_GET_AVERAGE_CNR
        key_col = "sat"

    pivoted_list = []
    for cnr_path in cnrs:
        conn = sqlite3.connect(cnr_path)
        df = pd.read_sql_query(sql, conn)
        conn.close()
        pivoted = df.pivot(index=key_col, columns="tna", values="avg_cnr")
        pivoted_list.append(pivoted)

    station_names = [cnr_path.name.split(".")[0] for cnr_path in cnrs]
    ref = pivoted_list[0]
    series_list = [ref.stack().rename(station_names[0])]
    for i, pivoted in enumerate(pivoted_list[1:], 1):
        diff = (pivoted - ref).stack().rename(station_names[i])
        series_list.append(diff)

    result = pd.concat(series_list, axis=1)
    result.index.names = [key_col, "tna"]
    result = result.dropna(subset=station_names[1:], how="all")
    return result
