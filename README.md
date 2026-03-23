# qoo-ip138

20260302 fork，修复脚本，适配 ip138 最新查询页面，改用 https://www.ipshudi.com/ 查询。

Python IP 地理位置信息查询工具（发布包名 `qoo-ip138`）。

## 安装

```bash
pip install qoo-ip138
```

## 命令行

```bash
qoo-ip138 --ip=172.217.161.164
```

## Python 调用

```python
from qoo_ip138 import qoo_ip138
qoo_ip138("111.111.111.111")
```

## 功能特性

- 支持 IP 地址地理位置查询
- 支持 JSON 输出格式
- 简单易用的命令行接口
- 纯 Python 实现，无浏览器依赖