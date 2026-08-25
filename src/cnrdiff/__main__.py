import argparse
from pathlib import Path

from . import __version__
from .api import FType, cnrconv, cnrdiff, detect_ftype


def main():
    parser = argparse.ArgumentParser(
        prog="cnrdiff",
        description="计算多测站相对于参考测站的载噪比差值",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    parser.add_argument(
        "files",
        nargs="+",
        help="观测数据文件列表，第一个文件为参考测站",
    )
    parser.add_argument(
        "--ftype",
        type=FType,
        default=None,
        help="观测数据文件类型（BNC_QC_LOG / RINEX3_OBS / RTCM3_MSM4），不指定则根据后缀自动识别",
    )
    parser.add_argument(
        "--by-sys",
        action="store_true",
        help="基于卫星系统计算载噪比差值",
    )
    parser.add_argument(
        "--no-cache",
        action="store_true",
        help="输出完成后删除过程中生成的 CNR 文件",
    )
    args = parser.parse_args()

    cnrs = []
    for fpath_str in args.files:
        fpath = Path(fpath_str)
        ftype = args.ftype or detect_ftype(fpath)
        cnr_path = cnrconv(fpath, ftype)
        cnrs.append(cnr_path)

    result = cnrdiff(cnrs, by_sys=args.by_sys)
    print(result.to_string())

    if args.no_cache:
        for cnr_path in cnrs:
            cnr_path.unlink()
