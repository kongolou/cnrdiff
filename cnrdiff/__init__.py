"""CNRDIFF

A library used to compare signal-to-noise ratio.

Include CNR file format conversion, difference calculation and plotting.

## Examples
The following examples use BNC QC LOG files. Note that RINEX V3 OBS files are also supported.

### Convert to CNR file
>>> cnrs = cnrdiff.log2cnr(['0002295h.log'])
>>> print(cnrs['0002295h.log.cnr'])

### Calculate difference with default parameters (mean of all epochs)
>>> logflist = ['0002295h.log', '0005295h.log', '0041295h.log']
>>> cnrs = cnrdiff.log2cnr(logflist)
>>> dcnrs = cnrdiff.cnr2dcnr(cnrs)
>>> print(dcnrs['0005295h.log.cnr.dcnr'])

### Calculate difference with custom parameters
>>> logflist = ['11121980.24O', '11131980.24O']
>>> dcnrflist = ['11121980.csv', '11131980.csv']
>>> start = datetime.datetime(2024, 7, 16, 9, 0, 0)
>>> end = datetime.datetime(2024, 7, 16, 10, 0, 0)
>>> interval = 5
>>> ele_cut = 20.0
>>> cnrdiff.log2cnr(logflist, save=False, start=start, end=end, interval=interval, ele_cut=ele_cut)
>>> cnrdiff.cnr2dcnr(cnrflist, save=dcnrflist, plot=True, how='MAX', by='SYS')

### Convert DCNR to XLSX file
>>> dcnrflist1 = ['0002295h.log.cnr.dcnr', '0005295h.log.cnr.dcnr', '0041295h.log.cnr.dcnr']
>>> dcnrflist2 = ['11121980.csv', '11131980.csv']
>>> cnrdiff.dcnr2xlsx([dcnrflist1, dcnrflist2], save='summary.xlsx')
"""

from cnrdiff.cnrdiff import log2cnr, rnx2cnr, cnr2dcnr, dcnr2xlsx

__version__ = "1.2.0"
__all__ = ["log2cnr", "rnx2cnr", "cnr2dcnr", "dcnr2xlsx"]
