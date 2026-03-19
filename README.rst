qoo-ip138
=========

20260302 fork，修复脚本，适配 ip138 最新查询页面，改用 https://www.ipshudi.com/ 查询。

Python IP 地理位置信息查询工具（仓库名 ``ip138``，发布包名 ``qoo-ip138``）。

安装
----

.. code-block:: bash

    pip install qoo-ip138

命令行
------

.. code-block:: bash

    qoo-ip138 --ip=172.217.161.164

兼容旧命令（也保留）
--------------------

.. code-block:: bash

    ip138 --ip=172.217.161.164

Python 调用
-----------

.. code-block:: python

    from ip138.ip138 import ip138
    ip138("111.111.111.111")
