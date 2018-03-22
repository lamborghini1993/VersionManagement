# -*- coding:utf-8 -*-
"""
@Author: xiaohao
@Date: 2018-03-22 16:01:18
@Desc:  打包脚本
"""

import os

sCurPath = os.getcwd()
print(sCurPath)

sCmd = "pyinstaller -w \
-n VersionManagement \
-i=./image/main.ico \
-F ./main.py"

os.system(sCmd)
