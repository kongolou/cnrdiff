import datetime
import os
import pandas as pd
import matplotlib.pyplot as plt
from typing import Literal


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
    plot: list[str] | bool = False,
    how: Literal["MEAN", "MAX"] = "MEAN",
    by: Literal["PRN", "SYS"] = "PRN",
) -> dict[str, pd.DataFrame]:
    """根据提供的 CNR 文件或缓存计算相应载噪比的差值.

    Parameters:
        read (list[str] | dict[str, pd.DataFrame]): 需要读取的 CNR 文件列表或 CNR 文件数据缓存.
        save (list[str] | bool, optional): 需要保存的 DCNR 文件列表或是否保存.
        plot (list[str] | bool, optional): 需要绘图的 DCNR 文件列表或是否绘图.
        how (Literal["MEAN", "MAX"], optional): 计算差值的方式.
        by (Literal["PRN", "SYS"], optional): 计算差值的方式.

    Returns:
        dict[str, pd.DataFrame]: DCNR 文件数据缓存.
    """
    if len(read) == 0:
        return {}
    # get raw dcnr
    if isinstance(read, dict):
        raw_cnr = read
    else:
        raw_cnr = {}
        for cnrfpath in read:
            raw_cnr[cnrfpath] = pd.read_csv(cnrfpath, header=None)
    # get pivoted dcnr
    pivoted_cnr = []
    for cnrfdata in raw_cnr.values():
        match by:
            case "PRN":
                cnrfdata.rename(columns={2: by}, inplace=True)
                buffer = []
                for i in range(4, cnrfdata.shape[1], 2):
                    pc_i = cnrfdata.pivot(index=[by, 0], columns=i, values=(i + 1))
                    buffer.append(pc_i)
            case "SYS":
                cnrfdata[1] = cnrfdata[2].str[0]
                cnrfdata.rename(columns={1: by}, inplace=True)
                buffer = []
                for i in range(4, cnrfdata.shape[1], 2):
                    pc_i = cnrfdata.pivot(index=[by, 2, 0], columns=i, values=(i + 1))
                    buffer.append(pc_i)
        match how:
            case "MEAN":
                pc = pd.concat(buffer).groupby(level=by).mean(numeric_only=True)
            case "MAX":
                pc = pd.concat(buffer).groupby(level=by).max(numeric_only=True)
        pc.dropna(axis=1, how="all", inplace=True)
        pivoted_cnr.append(pc)
    # calculate and save dcnr
    dcnr = {}
    if not isinstance(save, bool):
        dcnr[save[0]] = pivoted_cnr[0]
        for i, pc in enumerate(pivoted_cnr[1:], 1):
            dcnr[save[i]] = pc - pivoted_cnr[0]
        for dcnrfpath, dcnrfdata in dcnr.items():
            dcnrfdata.to_csv(dcnrfpath)
    elif save:
        save = [f"{cnrfpath}.dcnr" for cnrfpath in raw_cnr.keys()]
        dcnr[save[0]] = pivoted_cnr[0]
        for i, pc in enumerate(pivoted_cnr[1:], 1):
            dcnr[save[i]] = pc - pivoted_cnr[0]
        for dcnrfpath, dcnrfdata in dcnr.items():
            dcnrfdata.to_csv(dcnrfpath)
    else:
        save = [f"{cnrfpath}.dcnr" for cnrfpath in raw_cnr.keys()]
        dcnr[save[0]] = pivoted_cnr[0]
        for i, pc in enumerate(pivoted_cnr[1:], 1):
            dcnr[save[i]] = pc - pivoted_cnr[0]
    # plot dcnr
    if not isinstance(plot, bool):
        for dcnrfpath, dcnrfdata in dcnr.items():
            dcnrfdata.plot(king="bar", title=dcnrfpath)
            plt.savefig(dcnrfpath + ".png")
    elif plot:
        for dcnrfpath, dcnrfdata in dcnr.items():
            dcnrfdata.plot(kind="bar", title=dcnrfpath)
            plt.tight_layout()
            plt.show()

    return dcnr


def dcnr2xlsx(read: list[list[str]] | list[dict[str, pd.DataFrame]], save: str) -> None:
    workbook = []
    if isinstance(read[0], dict):
        workbook = read
    else:
        for dcnrflist in read:
            dcnr = {}
            for dcnrfpath in dcnrflist:
                dcnr[dcnrfpath] = pd.read_csv(dcnrfpath, index_col=0)
            workbook.append(dcnr)
    with pd.ExcelWriter(save) as writer:
        for sheet_i, dcnr in enumerate(workbook, 1):
            buffer = []
            for dcnrfpath, dcnrfdata in dcnr.items():
                dcnrfname = os.path.basename(dcnrfpath).split(".")[0]
                buffer.append(dcnrfdata.stack().rename(dcnrfname))
            pd.concat(buffer, axis=1).to_excel(writer, sheet_name=f"Group {sheet_i}")
