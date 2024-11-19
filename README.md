# CNRDIFF

A library used to compare signal-to-noise ratio.

Include CNR file format conversion, difference calculation and plotting.

**Lead Programmer:**
- Sheng Guoliang <shengguoliang@sinognss.com>

**Contributors:**
- Yang Fawang <yangfawang@sinognss.com>
- Wang Xiaobing <wangxiaobing@sinognss.com>

## History
| Date       | Version Info |
|------------|--------------|
| 2024-11-20 | Release 1.0  |

# Examples
## Convert to CNR file
```python
cnrs = cnrdiff.log2cnr(['0002295h.log'])
print(cnrs['0002295h.log.cnr'])
```
**Output:**
```
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
```
## Calculate difference with default parameters (mean of all epochs)
```python
logflist = ['0002295h.log', '0005295h.log', '0041295h.log']
cnrs = cnrdiff.log2cnr(logflist)
dcnrs = cnrdiff.cnr2dcnr(cnrs)
print(dcnrs['0005295h.log.cnr.dcnr'])
```
**Output:**
```
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
```
## Calculate difference with custom parameters
```python
logflist = ['11121980.24O', '11131980.24O']
dcnrflist = ['11121980.csv', '11131980.csv']
start = datetime.datetime(2024, 7, 16, 9, 0, 0)
end = datetime.datetime(2024, 7, 16, 10, 0, 0)
interval = 5  # doctest: +SKIP
ele_cut = 20.0  # doctest: +SKIP
cnrdiff.log2cnr(logflist, save=False, start=start, end=end, interval=interval, ele_cut=ele_cut)
cnrdiff.cnr2dcnr(cnrflist, save=dcnrflist, mode='max', plot=True)
```
## Further, save to XLSX file
```python
dcnrflist1 = ['0002295h.log.cnr.dcnr', '0005295h.log.cnr.dcnr']
dcnrflist2 = ['0002295h.log.cnr.dcnr', '0041295h.log.cnr.dcnr']
xlsxfpath = '0002295h.log.cnr.dcnr.xlsx'
cnrdiff.dcnr2xlsx([dcnrflist1, dcnrflist2], xlsxfpath, mode='mean')
```
