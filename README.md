# CNRDIFF

A library used to compare signal-to-noise ratio.（卫星载噪比差值比较）

## 依赖项

- pyrtcm
- pandas

## 使用方法

计算 SN04 和 SN02 测站相对于 SN01 测站的载噪比差值

```bash
cnrdiff SN01001a.24O SN02001a.24O SN04001a.24O
```

### 自定义参数

基于卫星系统计算载噪比差值 b - a，并将输出保存到文件里

```bash
cnrdiff --ftype RTCM3_MSM4 a.bin b.bin --by-sys > result.txt
```

## 平均值算法

### 基本假设

1. 各测站观测数据正常记录，无历元缺失，无事件干扰
2. 各测站观测数据时间同步，起止时间尽量一致
3. 各测站观测数据历元间隔不超过 1s，实际按 1s 间隔处理

### 基于卫星号（默认）

运行过程中所产生的 CNR 二进制文件是一个 SQLite 数据库文件，存储逐一历元逐一卫星逐一频点下的载噪比

1. 先**对各卫星全历元求各频点平均**，得到以卫星号和频点作为行列的数据表
2. 再**对各测站数据表进行对齐后做差**，得到以卫星号+频点和测站（数据文件名）作为行列的数据表


### 基于卫星系统

从卫星号中提取卫星系统，作为新的维度

1. 先**对各卫星系统全卫星全历元求各频点平均（等价于各卫星根据历元数加权平均）**，得到以卫星系统和频点作为行列的数据表
2. 再**对各测站数据表进行对齐后做差**，得到以卫星系统+频点和测站（数据文件名）作为行列的数据表

## 许可证

MIT

## 作者及贡献名单

**Lead Programmer:**
Sheng Guoliang <shengguoliang@sinognss.com>

**Contributors:**
- Yang Fawang <yangfawang@sinognss.com>
