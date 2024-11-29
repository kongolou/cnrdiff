"""CNRDIFF

A library used to compare signal-to-noise ratio.

Include CNR file format conversion, difference calculation and plotting.

**Lead Programmer:**
    Sheng Guoliang <shengguoliang@sinognss.com>

**Contributors:**
    Yang Fawang <yangfawang@sinognss.com>
    Wang Xiaobing <wangxiaobing@sinognss.com>

# History
|            |             |
|------------|-------------|
| 2024-11-20 | Release 1.0 |
| 2024-11-29 | Release 1.1 |

# Examples
## Convert to CNR file
>>> cnrs = cnrdiff.log2cnr(['0002295h.log'])  # doctest: +SKIP
>>> print(cnrs['0002295h.log.cnr'])  # doctest: +SKIP
                         0     1    2      3    4     5    6     7     8     9     10    11
0       2024-10-21T08:00:00     1  G03   0.00  S1C  40.0  S2C  45.0   S2W  40.0   S5I  46.0
1       2024-10-21T08:00:00     1  G16   0.00  S1C  44.0  S2W  34.0  None   NaN  None   NaN
2       2024-10-21T08:00:00     1  G26  72.19  S1C  48.0  S2C  48.0   S2W  49.0   S5I  49.0
3       2024-10-21T08:00:00     1  G28  54.10  S1C  44.0  S2C  49.0   S2W  36.0   S5I  49.0
4       2024-10-21T08:00:00     1  G29  29.28  S1C  38.0  S2C  33.0   S2W  23.0  None   NaN
...                     ...   ...  ...    ...  ...   ...  ...   ...   ...   ...   ...   ...
154214  2024-10-21T09:00:00  3601  C39  69.81  S2I  49.0  S6I  47.0  None   NaN  None   NaN
154215  2024-10-21T09:00:00  3601  C40  50.54  S2I  47.0  S6I  47.0  None   NaN  None   NaN
154216  2024-10-21T09:00:00  3601  C45  40.91  S2I  47.0  S6I  49.0  None   NaN  None   NaN
154217  2024-10-21T09:00:00  3601  C59  47.34  S2I  47.0  S6I  48.0  None   NaN  None   NaN
154218  2024-10-21T09:00:00  3601  C60  31.67  S2I  43.0  S6I  45.0  None   NaN  None   NaN

[154219 rows x 12 columns]

## Calculate difference with default parameters (mean of all epochs)
>>> logflist = ['0002295h.log', '0005295h.log', '0041295h.log']  # doctest: +SKIP
>>> cnrs = cnrdiff.log2cnr(logflist)  # doctest: +SKIP
>>> dcnrs = cnrdiff.cnr2dcnr(cnrs)  # doctest: +SKIP
>>> print(dcnrs['0005295h.log.cnr.dcnr'])  # doctest: +SKIP
          S1C       S1X       S2C       S2I       S2P       S6I       S7I       S2W       S5I       S5X       S7X
PRN
C01       NaN       NaN       NaN -0.940572       NaN  0.085532 -0.843655       NaN       NaN       NaN       NaN
C02       NaN       NaN       NaN -1.191891       NaN  0.429325 -0.875868       NaN       NaN       NaN       NaN
C03       NaN       NaN       NaN -0.871425       NaN  0.767287 -0.167453       NaN       NaN       NaN       NaN
C04       NaN       NaN       NaN -1.157456       NaN -0.718967 -0.314079       NaN       NaN       NaN       NaN
C06       NaN       NaN       NaN -0.649542       NaN  0.709525 -0.185782       NaN       NaN       NaN       NaN
C07       NaN       NaN       NaN -0.628992       NaN -0.109414 -0.797001       NaN       NaN       NaN       NaN
C08       NaN       NaN       NaN -7.029925       NaN -7.659138 -8.090604       NaN       NaN       NaN       NaN
C09       NaN       NaN       NaN -0.430158       NaN  0.553180 -0.311580       NaN       NaN       NaN       NaN
C10       NaN       NaN       NaN -0.613441       NaN -0.668148 -1.409331       NaN       NaN       NaN       NaN
C13       NaN       NaN       NaN -0.420030       NaN -0.170935 -1.856699       NaN       NaN       NaN       NaN
C16       NaN       NaN       NaN -0.250764       NaN  0.668981 -0.287420       NaN       NaN       NaN       NaN
C19       NaN       NaN       NaN -0.715357       NaN -0.722855       NaN       NaN       NaN       NaN       NaN
C21       NaN       NaN       NaN -0.637597       NaN -0.221556       NaN       NaN       NaN       NaN       NaN
C22       NaN       NaN       NaN -1.140517       NaN  0.246876       NaN       NaN       NaN       NaN       NaN
C27       NaN       NaN       NaN -0.660690       NaN  0.482968       NaN       NaN       NaN       NaN       NaN
C29       NaN       NaN       NaN -1.968718       NaN -0.774428       NaN       NaN       NaN       NaN       NaN
C30       NaN       NaN       NaN -1.069425       NaN -0.106082       NaN       NaN       NaN       NaN       NaN
C36       NaN       NaN       NaN -0.360178       NaN  0.860317       NaN       NaN       NaN       NaN       NaN
C38       NaN       NaN       NaN -1.204633       NaN -0.822394       NaN       NaN       NaN       NaN       NaN
C39       NaN       NaN       NaN -0.246876       NaN  0.602888       NaN       NaN       NaN       NaN       NaN
C40       NaN       NaN       NaN -0.486254       NaN -0.064704       NaN       NaN       NaN       NaN       NaN
C45       NaN       NaN       NaN -1.191613       NaN -0.384615       NaN       NaN       NaN       NaN       NaN
C59       NaN       NaN       NaN -0.490419       NaN  0.075257       NaN       NaN       NaN       NaN       NaN
C60       NaN       NaN       NaN -0.384060       NaN -1.341294       NaN       NaN       NaN       NaN       NaN
E02       NaN  0.028881       NaN       NaN       NaN       NaN       NaN       NaN       NaN  0.704249  0.470425
E03       NaN -1.054074       NaN       NaN       NaN       NaN       NaN       NaN       NaN  0.616438 -0.138428
E07       NaN -0.602333       NaN       NaN       NaN       NaN       NaN       NaN       NaN  0.645376  0.058595
E08       NaN -0.708137       NaN       NaN       NaN       NaN       NaN       NaN       NaN  0.638156 -0.257706
E27       NaN -0.317690       NaN       NaN       NaN       NaN       NaN       NaN       NaN -0.507359 -1.391002
E29       NaN -0.891760       NaN       NaN       NaN       NaN       NaN       NaN       NaN -0.697708 -1.014139
E30       NaN -0.801444       NaN       NaN       NaN       NaN       NaN       NaN       NaN  0.892252  0.099417
G03 -1.185782       NaN -1.468857       NaN       NaN       NaN       NaN -1.909297 -0.956679       NaN       NaN
G04 -1.012480       NaN -1.029914       NaN       NaN       NaN       NaN -1.265208 -0.205828       NaN       NaN
G16 -1.130242       NaN       NaN       NaN       NaN       NaN       NaN -1.521244       NaN       NaN       NaN
G26 -0.423493       NaN  0.109136       NaN       NaN       NaN       NaN -0.277978  0.285754       NaN       NaN
G27 -0.928958       NaN -1.408960       NaN       NaN       NaN       NaN -2.466618 -0.895877       NaN       NaN
G28 -0.141905       NaN  0.383505       NaN       NaN       NaN       NaN  0.147459  0.844210       NaN       NaN
G29 -1.328652       NaN -0.748343       NaN       NaN       NaN       NaN -1.765429       NaN       NaN       NaN
G31 -0.170786       NaN  0.321577       NaN       NaN       NaN       NaN  0.034713       NaN       NaN       NaN
G32 -1.343793       NaN -0.820605       NaN       NaN       NaN       NaN -2.168564 -0.294085       NaN       NaN
R04 -0.536518       NaN       NaN       NaN -1.141905       NaN       NaN       NaN       NaN       NaN       NaN
R05 -0.286865       NaN       NaN       NaN  0.102194       NaN       NaN       NaN       NaN       NaN       NaN
R06       NaN       NaN       NaN       NaN       NaN       NaN       NaN       NaN       NaN       NaN       NaN
R14 -1.866949       NaN       NaN       NaN -1.413515       NaN       NaN       NaN       NaN       NaN       NaN
R15 -0.825326       NaN       NaN       NaN  0.395446       NaN       NaN       NaN       NaN       NaN       NaN
R16 -2.187170       NaN       NaN       NaN -0.758400       NaN       NaN       NaN       NaN       NaN       NaN
R17 -0.660695       NaN       NaN       NaN -0.220414       NaN       NaN       NaN       NaN       NaN       NaN
R18 -2.040590       NaN       NaN       NaN  0.568744       NaN       NaN       NaN       NaN       NaN       NaN
R24 -1.121621       NaN       NaN       NaN -0.724670       NaN       NaN       NaN       NaN       NaN       NaN

## Calculate difference with custom parameters
>>> logflist = ['11121980.24O', '11131980.24O']  # doctest: +SKIP
>>> dcnrflist = ['11121980.csv', '11131980.csv']  # doctest: +SKIP
>>> start = datetime.datetime(2024, 7, 16, 9, 0, 0)  # doctest: +SKIP
>>> end = datetime.datetime(2024, 7, 16, 10, 0, 0)  # doctest: +SKIP
>>> interval = 5  # doctest: +SKIP
>>> ele_cut = 20.0  # doctest: +SKIP
>>> cnrdiff.log2cnr(logflist, save=False, start=start, end=end, interval=interval, ele_cut=ele_cut)  # doctest: +SKIP
>>> cnrdiff.cnr2dcnr(cnrflist, save=dcnrflist, mode='max', plot=True)  # doctest: +SKIP

"""

import datetime
import pandas as pd
import matplotlib.pyplot as plt


__version__ = "1.1.0"


def log2cnr(
    read: list[str],
    save: list[str] | bool = False,
    start: datetime.datetime | None = None,
    end: datetime.datetime | None = None,
    interval: datetime.timedelta | float | int | None = None,
    ele_cut: float = 0.0,
) -> dict[str, pd.DataFrame]:
    """将 BNC QC LOG 文件转换为 CNR 格式.

    读取策略：
    1. 读两遍文件。第一遍核对时间，第二遍存储数据.
    2. 不指定起始时刻，默认起始时刻为文件中首次出现记录的时刻.
    3. 不指定结束时刻，默认结束时刻为文件中最后一次记录的时刻.
    4. 不指定历元间隔，默认历元间隔为文件中所有相邻时刻间隔的最小值.
    5. 不指定高度截止角阈值，默认高度截止角阈值为 0.0°.
    6. 历元缺失，则缺省记录，不会抛出异常.
    7. 指定时间范围非法，抛出异常.
    8. 指定高度截止角阈值非法，抛出异常.

    Parameters:
        read (list[str]): 需要读取的 BNC QC LOG 文件列表.
        save (list[str] | bool, optional): 需要保存的 CNR 文件列表或是否保存.
        start (datetime.datetime | None, optional): 起始时刻.
        end (datetime.datetime | None, optional): 结束时刻.
        interval (datetime.timedelta | float | int | None, optional): 历元间隔.
        ele_cut (float = 0.0, optional): 高度截止角阈值.

    Returns:
        dict[str, pd.DataFrame]: CNR 文件数据缓存.

    Raises:
        ValueError: 指定时间范围非法.
        ValueError: 指定高度截止角阈值非法.
    """
    result = {}
    for logfpath in read:
        # --------第一次读取：核对时间信息--------
        have = []
        with open(logfpath, "r") as fr:
            for line in fr:
                if line.startswith(">"):
                    have.append(
                        datetime.datetime(
                            year=int(line[2:6]),
                            month=int(line[7:9]),
                            day=int(line[10:12]),
                            hour=int(line[13:15]),
                            minute=int(line[16:18]),
                            second=int(line[19:21]),
                            microsecond=int(line[22:28]),
                        )
                    )
        # 读取策略 2
        if start is None:
            start = have[0]
        if isinstance(interval, int) or isinstance(interval, float):
            interval = datetime.timedelta(seconds=interval)
        # 读取策略 4
        if interval is None:
            temp = []
            for i, j in zip(have[1:], have[:-1]):
                temp.append(i - j)
            interval = min(temp)
        # 读取策略 3
        if end is None:
            end = have[-1] + interval
        expt = [(start + interval * i) for i in range((end - start) // interval)]
        have, expt = pd.Series(have), pd.Series(expt)
        use = expt[expt.isin(have)]
        # 读取策略 7
        if use.empty:
            raise ValueError("Invalid time range.")
        # --------第二次读取：存储卫星数据--------
        # 读取策略 6
        epoch = (use.index + 1).values
        use.reset_index(drop=True, inplace=True)
        cnr_buf = []
        with open(logfpath, "r") as fr:
            idx = 0
            flag = 0  # 当前时间节点未记录存储的卫星数
            for line in fr:
                # 将卫星数据一颗颗写入缓存
                if flag != 0:
                    data = line.split()
                    row = [use[idx].isoformat(), epoch[idx], data[0], float(data[1])]
                    obsn = int(data[3]) // 2
                    for i in range(obsn):
                        row.append("S" + data[4 + i * 6][1:3])  # 更正观测类型代码
                        row.append(float(data[6 + i * 6]))
                    cnr_buf.append(row)
                    flag -= 1
                    if flag == 0:
                        idx += 1
                if line.startswith(">"):
                    if idx == use.size:
                        break
                    moment = datetime.datetime(
                        year=int(line[2:6]),
                        month=int(line[7:9]),
                        day=int(line[10:12]),
                        hour=int(line[13:15]),
                        minute=int(line[16:18]),
                        second=int(line[19:21]),
                        microsecond=int(line[22:28]),
                    )
                    if moment == use[idx]:
                        flag = int(line[30:32])
        cnr = pd.DataFrame(cnr_buf)
        # 读取策略 5, 8
        if 0.0 <= ele_cut <= 90.0:
            cnr = cnr[cnr[3] >= ele_cut]
        else:
            raise ValueError("Invalid elevation angle cut-off.")
        cnrfpath = logfpath + ".cnr"
        result[cnrfpath] = cnr

    if not isinstance(save, bool):
        for cnr, cnrfpath in zip(result.values(), save):
            cnr.to_csv(cnrfpath, index=False, header=False)
    elif save:
        for cnr, logfpath in zip(result.values(), read):
            cnrfpath = f"{logfpath}.cnr"
            cnr.to_csv(cnrfpath, index=False, header=False)

    return result


def rnx2cnr(
    read: list[str],
    save: list[str] | bool = False,
    start: datetime.datetime | None = None,
    end: datetime.datetime | None = None,
    interval: datetime.timedelta | float | int | None = None,
    ele_cut: float = 0.0,
) -> dict[str, pd.DataFrame]:
    """将 RINEX V3 OBS 文件转换为 CNR 格式."""
    result = {}
    for rnxfpath in read:
        # -------- Round 1 --------
        tna = {}
        have = []
        with open(rnxfpath, "r") as fr:
            line0_buf = " "
            for line in fr:
                if "SYS / # / OBS TYPES" in line:
                    temp = line[7:59].split()
                    if line[0] != " ":
                        tna[line[0]] = temp
                        line0_buf = line[0]
                    else:
                        tna[line0_buf] += temp
                if line.startswith(">"):
                    have.append(
                        datetime.datetime(
                            year=int(line[2:6]),
                            month=int(line[7:9]),
                            day=int(line[10:12]),
                            hour=int(line[13:15]),
                            minute=int(line[16:18]),
                            second=int(line[19:21]),
                            microsecond=int(line[22:28]),
                        )
                    )
        if start is None:
            start = have[0]
        if isinstance(interval, int) or isinstance(interval, float):
            interval = datetime.timedelta(seconds=interval)
        if interval is None:
            temp = []
            for i, j in zip(have[1:], have[:-1]):
                temp.append(i - j)
            interval = min(temp)
        if end is None:
            end = have[-1] + interval
        expt = [(start + interval * i) for i in range((end - start) // interval)]
        have, expt = pd.Series(have), pd.Series(expt)
        use = expt[expt.isin(have)]
        if use.empty:
            raise ValueError("Invalid time range.")
        # -------- Round 2 --------
        epoch = (use.index + 1).values
        use.reset_index(drop=True, inplace=True)
        cnr_buf = []
        with open(rnxfpath, "r") as fr:
            idx = 0
            flag = 0
            tna_val = {}
            for line in fr:
                if flag != 0:
                    tna_val[line[0]] = [
                        line[i : (i + 16)] for i in range(1, len(line), 16)
                    ]
                    row = [
                        use[idx].isoformat(),
                        epoch[idx],
                        line[0:3],
                        90.0,
                    ]  # TODO: 90.0
                    for i, tna_label in enumerate(tna[line[0]]):
                        if tna_label.startswith("S"):
                            row.append(tna[line[0]][i])
                            val = tna_val[line[0]][i][10:16].replace(" ", "")
                            val = float(val) if val != "" else None
                            row.append(val)
                    cnr_buf.append(row)
                    flag -= 1
                    if flag == 0:
                        idx += 1
                if line.startswith(">"):
                    if idx == use.size:
                        break
                    moment = datetime.datetime(
                        year=int(line[2:6]),
                        month=int(line[7:9]),
                        day=int(line[10:12]),
                        hour=int(line[13:15]),
                        minute=int(line[16:18]),
                        second=int(line[19:21]),
                        microsecond=int(line[22:28]),
                    )
                    if moment == use[idx]:
                        flag = int(line[33:35])
        cnr = pd.DataFrame(cnr_buf)
        if 0.0 <= ele_cut <= 90.0:
            cnr = cnr[cnr[3] >= ele_cut]
        else:
            raise ValueError("Invalid elevation angle cut-off.")
        cnrfpath = rnxfpath + ".cnr"
        result[cnrfpath] = cnr

    if not isinstance(save, bool):
        for cnr, cnrfpath in zip(result.values(), save):
            cnr.to_csv(cnrfpath, index=False, header=False)
    elif save:
        for cnr, rnxfpath in zip(result.values(), read):
            cnrfpath = f"{rnxfpath}.cnr"
            cnr.to_csv(cnrfpath, index=False, header=False)

    return result


def cnr2dcnr(
    read: list[str] | dict[str, pd.DataFrame],
    save: list[str] | bool = False,
    mode: str = "mean",
    plot: bool = False,
) -> dict[str, pd.DataFrame]:
    """根据提供的 CNR 文件或缓存计算相应载噪比的差值.

    Parameters:
        read (list[str] | dict[str, pd.DataFrame]): 需要读取的 CNR 文件列表或 CNR 文件数据缓存.
        save (list[str] | bool, optional): 需要保存的 DCNR 文件列表或是否保存.
        mode (str, optional): 计算差值的方式, 可选 "mean" 或 "max".
        plot (bool, optional): 是否绘制差值图.

    Returns:
        dict[str, pd.DataFrame]: DCNR 文件数据缓存.

    Raises:
        ValueError: 如果 mode 不是 "mean" 或 "max".
    """
    if len(read) == 0:
        return {}

    raw_cnrs = {}
    if isinstance(read, dict):
        raw_cnrs = read
    else:
        for cnrfpath in read:
            raw_cnrs[cnrfpath] = pd.read_csv(cnrfpath, header=None)

    dcnrflist = []
    pivoted_cnrs = []
    for cnrfpath, raw_cnr in raw_cnrs.items():
        raw_cnr.rename(columns={2: "PRN"}, inplace=True)
        buffer = []
        for j in range(4, raw_cnr.shape[1], 2):
            pivoted_cnr = raw_cnr.pivot(index=["PRN", 0], columns=j, values=(j + 1))
            buffer.append(pivoted_cnr)
        match mode.lower():
            case "mean":
                pivoted_cnr = (
                    pd.concat(buffer).groupby(level="PRN").mean(numeric_only=True)
                )
            case "max":
                pivoted_cnr = (
                    pd.concat(buffer).groupby(level="PRN").max(numeric_only=True)
                )
            case _:
                raise ValueError(f"Unknown mode: {mode}.")
        pivoted_cnr.dropna(axis=1, how="all", inplace=True)
        pivoted_cnrs.append(pivoted_cnr)
        dcnrflist.append(cnrfpath + ".dcnr")

    result = {}
    result[dcnrflist[0]] = pivoted_cnrs[0]
    for key, value in zip(dcnrflist[1:], pivoted_cnrs[1:]):
        result[key] = value - pivoted_cnrs[0]

    if not isinstance(save, bool):
        for dcnr, dcnrfpath in zip(result.values(), save):
            dcnr.to_csv(dcnrfpath)
    elif save:
        for dcnrfpath, dcnr in result.items():
            dcnr.to_csv(dcnrfpath)

    if plot:
        for key, value in result.items():
            value.plot(kind="bar", title=key)
            plt.tight_layout()
            plt.show()

    return result
