# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwidget.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1042, 712)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBoxPubType = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxPubType.setObjectName("comboBoxPubType")
        self.horizontalLayout.addWidget(self.comboBoxPubType)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEditVersionConfig = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditVersionConfig.setReadOnly(True)
        self.lineEditVersionConfig.setObjectName("lineEditVersionConfig")
        self.horizontalLayout.addWidget(self.lineEditVersionConfig)
        self.pushButtonVersionConfig = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonVersionConfig.setObjectName("pushButtonVersionConfig")
        self.horizontalLayout.addWidget(self.pushButtonVersionConfig)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 5)
        self.horizontalLayout.setStretch(5, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.comboBoxProject = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxProject.setObjectName("comboBoxProject")
        self.horizontalLayout_2.addWidget(self.comboBoxProject)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.lineEditScriptDir = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditScriptDir.setReadOnly(True)
        self.lineEditScriptDir.setObjectName("lineEditScriptDir")
        self.horizontalLayout_2.addWidget(self.lineEditScriptDir)
        self.pushButtonScriptPath = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonScriptPath.setObjectName("pushButtonScriptPath")
        self.horizontalLayout_2.addWidget(self.pushButtonScriptPath)
        self.horizontalLayout_2.setStretch(1, 2)
        self.horizontalLayout_2.setStretch(2, 2)
        self.horizontalLayout_2.setStretch(3, 1)
        self.horizontalLayout_2.setStretch(4, 5)
        self.horizontalLayout_2.setStretch(5, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBoxModule = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxModule.setObjectName("groupBoxModule")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBoxModule)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBoxModule)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEditModuleSearch = QtWidgets.QLineEdit(self.groupBoxModule)
        self.lineEditModuleSearch.setObjectName("lineEditModuleSearch")
        self.horizontalLayout_4.addWidget(self.lineEditModuleSearch)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.treeWidgetModule = QtWidgets.QTreeWidget(self.groupBoxModule)
        self.treeWidgetModule.setObjectName("treeWidgetModule")
        self.verticalLayout_2.addWidget(self.treeWidgetModule)
        self.horizontalLayout_3.addWidget(self.groupBoxModule)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonAddModule = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAddModule.setObjectName("pushButtonAddModule")
        self.verticalLayout.addWidget(self.pushButtonAddModule)
        self.pushButtonAllNewModule = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonAllNewModule.setObjectName("pushButtonAllNewModule")
        self.verticalLayout.addWidget(self.pushButtonAllNewModule)
        self.pushButtonDelModule = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonDelModule.setObjectName("pushButtonDelModule")
        self.verticalLayout.addWidget(self.pushButtonDelModule)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tableWidgetModule = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidgetModule.setAutoFillBackground(True)
        self.tableWidgetModule.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetModule.setProperty("showDropIndicator", False)
        self.tableWidgetModule.setAlternatingRowColors(True)
        self.tableWidgetModule.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidgetModule.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetModule.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidgetModule.setObjectName("tableWidgetModule")
        self.tableWidgetModule.setColumnCount(2)
        self.tableWidgetModule.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetModule.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetModule.setHorizontalHeaderItem(1, item)
        self.tableWidgetModule.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidgetModule.horizontalHeader().setMinimumSectionSize(21)
        self.tableWidgetModule.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetModule.verticalHeader().setVisible(False)
        self.horizontalLayout_5.addWidget(self.tableWidgetModule)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.pushButtonExport = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonExport.setObjectName("pushButtonExport")
        self.horizontalLayout_6.addWidget(self.pushButtonExport)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.pushButtonExist = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonExist.setObjectName("pushButtonExist")
        self.horizontalLayout_6.addWidget(self.pushButtonExist)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1042, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "版本管理工具"))
        self.label_2.setText(_translate("MainWindow", "公共类型:"))
        self.label_4.setText(_translate("MainWindow", "    版本配置选择:"))
        self.pushButtonVersionConfig.setText(_translate("MainWindow", "文件选择"))
        self.label_3.setText(_translate("MainWindow", "项目代号:"))
        self.label_5.setText(_translate("MainWindow", "脚本导出路径选择:"))
        self.pushButtonScriptPath.setText(_translate("MainWindow", "路径选择"))
        self.groupBoxModule.setTitle(_translate("MainWindow", "模块选择"))
        self.label.setText(_translate("MainWindow", "搜索： "))
        self.treeWidgetModule.headerItem().setText(0, _translate("MainWindow", "模块名"))
        self.pushButtonAddModule.setText(_translate("MainWindow", "增加"))
        self.pushButtonAllNewModule.setText(_translate("MainWindow", "全选最新"))
        self.pushButtonDelModule.setText(_translate("MainWindow", "删除"))
        self.groupBox_2.setTitle(_translate("MainWindow", "已选模块——待导出"))
        item = self.tableWidgetModule.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "模块名"))
        item = self.tableWidgetModule.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "版本号"))
        self.pushButtonExport.setText(_translate("MainWindow", "导出"))
        self.pushButtonExist.setText(_translate("MainWindow", "退出"))
