# -*- coding: utf-8 -*-

import os
import sys
import logging
import task, db

from mytool import pubdefines

def InitConfig():
    if not os.path.exists("xh"):
        os.makedirs("xh")
    sLogDir = os.path.join(os.getcwd(), "log")
    pubdefines.makedirs(sLogDir)
    logging.basicConfig(
        filename = "log/log%s.log" % pubdefines.time_to_str(timeformat="%Y-%m-%d %H-%M-%S"),
        format = "[%(asctime)s] [%(levelname)s] [%(filename)s] [%(lineno)s] %(message)s",
        datefmt = "%Y-%m-%d %H:%M:%S",
        level = logging.DEBUG,
    )
    ch = logging.StreamHandler()
    logger = logging.getLogger()
    logger.addHandler(ch)
    logging.info("init config...")


def InitManager():
    db.InitDB()
    task.InitTask()
    logging.info("init manager...")


def Start():
    InitConfig()
    InitManager()
    task.Show()

if __name__ == "__main__":
    Start()

