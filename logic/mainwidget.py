# -*- coding:utf-8 -*-
"""
@Author: xiaohao
@Date: 2018-03-21 11:41:34
@Desc: 
"""

import sys
import os

from PyQt5 import QtWidgets, QtCore, QtGui
from ui import mainwidget
from . import misc

PERSON_CONFIG = "person.json"
COMMON_CONFIG = "common.json"
LST_PUB_TYPE = ["pubdy3d"]
LST_PROJECT = ["MarsEditor", "DramaEditor", "UIEditor", "T2MapEditor"]
PUT_PATH_INFO = {
    "pubdy3d"   : r"D:\mycode\exe\pubdy3d"
}


class CMainWidget(QtWidgets.QMainWindow, mainwidget.Ui_MainWindow):
    def __init__(self, *args):
        super(CMainWidget, self).__init__(*args)
        self.setupUi(self)
        self.m_PersonConfig = {}    #个人配置信息
        self.m_CommonConfig = {}    #通用配置信息
        self.m_ModuleInfo = {}      #当前模块对应的版本
        self.m_ModuleList = []      #[(模块名, 版本), ]
        self.m_ScriptDir = ""       #脚本导出存放目录
        self.m_VersionConfigPath = ""   #版本配置文件
        self.InitConfig()
        self.InitUI()
        self.InitConnect()


    def InitConfig(self):
        self.m_PersonConfig = misc.JsonLoad(PERSON_CONFIG, {})
        self.m_CommonConfig = misc.JsonLoad(COMMON_CONFIG, {})



    def InitUI(self):
        lstPubType = self.m_CommonConfig.get("pubtype", LST_PUB_TYPE)
        lstProject = self.m_CommonConfig.get("pubtype", LST_PROJECT)
        self.comboBoxPubType.addItems(lstPubType)
        self.comboBoxProject.addItems(lstProject)

        sLastType = self.m_PersonConfig.get("lasttype", "")
        if sLastType:
            self.comboBoxPubType.setCurrentText(sLastType)
        dTypeInfo = self.m_PersonConfig.get(sLastType, {})
        sLastProject = dTypeInfo.get("lastproject", "")
        if sLastProject:
            self.comboBoxPubType.setCurrentText(sLastProject)
        dProjectInfo = dTypeInfo.get(sLastProject, {})
        self.m_ScriptDir = dProjectInfo.get("scriptpath", os.getcwd())
        self.lineEditScriptDir.setText(self.m_ScriptDir)

        # sPubType = self.comboBoxPubType.currentText()
        # self.m_PubPath = self.m_CommonConfig[sPubType]
        # self.ShowModuleTableWidget()


    def InitConnect(self):
        self.pushButtonVersionConfig.clicked.connect(self.ChooseVersionConfig)
        self.pushButtonScriptPath.clicked.connect(self.ChooseSciptPath)
        self.pushButtonExport.clicked.connect(self.ModuleExport)


    def ChooseVersionConfig(self):
        """版本配置文件选择"""
        sFile = QtWidgets.QFileDialog.getOpenFileName(self, "版本配置文件选择", "", "Json文件(*.json)")[0]
        self.lineEditVersionConfig.setText(sFile)
        if sFile:
            self.InitModuleTableWidget(sFile)
            self.ShowModuleTableWidget()
            self.m_VersionConfigPath = sFile


    def ChooseSciptPath(self):
        """选择脚本导出到那个路径"""
        sDir = QtWidgets.QFileDialog.getExistingDirectory(self, "脚本导出路径选择", "")
        self.lineEditScriptDir.setText(sDir)
        if sDir:
            self.m_ScriptDir = sDir


    def InitModuleTreeWidget(self):
        pass


    def InitModuleTableWidget(self, sFile):
        """从配置读取版本信息，然后加载"""
        dModule = {}
        gg_ModuleInfo = misc.JsonLoad(sFile, {})
        for sModule, dInfo in gg_ModuleInfo.items():
            sVersion = dInfo["version"]
            if sVersion in dModule and dModule[sModule] != sVersion:
                print("冲突 %s %s %s" % (sModule, sVersion, dModule[sModule]))
                return
            dModule[sModule] = sVersion
            for key, value in dInfo.items():
                if key in ("version", "svn_path"):
                    continue
                if key in dModule and dModule[key] != value:
                    print("冲突 %s %s %s %s" % (sModule, key, sVersion, dModule[key]))
                    return
                dModule[key] = value
        self.m_ModuleInfo = dModule


    def ShowModuleTableWidget(self):
        self.m_ModuleList = sorted(self.m_ModuleInfo.items(), key=lambda x:x[0])
        self.tableWidgetModule.clearContents()
        self.tableWidgetModule.setRowCount(len(self.m_ModuleList))
        for iIndex, (sModule, sVersion) in enumerate(self.m_ModuleList):
            oModuleItem = QtWidgets.QTableWidgetItem(sModule)
            oVersionItem = QtWidgets.QTableWidgetItem(sVersion)
            self.tableWidgetModule.setItem(iIndex, 0, oModuleItem)
            self.tableWidgetModule.setItem(iIndex, 1, oVersionItem)


    def ModuleExport(self):
        """模块导出"""
        s1 = self.comboBoxPubType.currentText()
        s2 = self.comboBoxProject.currentText()
        destinationDir = os.path.join(self.m_ScriptDir, s1 + "_" + s2)
        # if not os.path.exists(destinationDir):
        #     os.makedirs(destinationDir)
        sourcePath = r"D:\mycode\exe\pubdy3d"
        for (sModule, sVersion) in self.m_ModuleList:
            sourceFile = os.path.join(sourcePath, sModule, sVersion)
            destinationFile = os.path.join(destinationDir, sModule, sVersion)
            print("source:", sourceFile)
            print("\t", destinationFile)




def Show():
    app = QtWidgets.QApplication(sys.argv)
    obj = CMainWidget()
    obj.show()
    sys.exit(app.exec_())
