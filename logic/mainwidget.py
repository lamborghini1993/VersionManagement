# -*- coding:utf-8 -*-
"""
@Author: xiaohao
@Date: 2018-03-21 11:41:34
@Desc: 
"""

from PyQt5 import QtWidgets, QtCore, QtGui
from ui import mainwidget


class CMainWidget(QtWidgets.QMainWindow, mainwidget.Ui_MainWindow):
    def __init__(self, *args):
        super(CMainWidget, self).__init__(*args)
        self.setupUi(self)
