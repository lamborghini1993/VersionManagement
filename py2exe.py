# -*- coding:utf-8 -*-
"""
@Author: xiaohao
@Date: 2018-03-22 16:01:18
@Desc:  打包脚本
"""

import os
import shutil

sName = "VersionManagement"

sCmd = "pyinstaller -w \
-n %s \
-i=./image/main.ico \
-F ./main.py" % sName

os.system(sCmd)
shutil.move("dist/%s.exe" % sName, "%s.exe" % sName)
shutil.rmtree("build")
shutil.rmtree("dist")
os.remove("%s.spec" % sName)
