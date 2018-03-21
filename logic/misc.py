# -*- coding:utf-8 -*-
"""
@Author: xiaohao
@Date: 2018-03-21 13:51:13
@Desc: 各种通用函数
"""

import json
import os

def JsonDump(data, path, **myArgs):
    dJsonArgs = {
        "ensure_ascii"  : False,
        "allow_nan"     : False,
        "indent"        : 4,
    }
    dJsonArgs.update(myArgs)
    coding = dJsonArgs.pop("encoding", "utf-8")
    with open(path, "w", encoding=coding) as fp:
        json.dump(data, fp, **dJsonArgs)


def JsonLoad(path, default=None, **myArgs):
    if not os.path.exists(path):
        return default
    coding = myArgs.pop("encoding", "utf-8")
    with open(path, "r", encoding=coding) as fp:
        default = json.load(fp, **myArgs)
    return default
