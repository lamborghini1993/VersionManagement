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

PERSON_CONFIG = "config/person.config"
COMMON_CONFIG = "config/common.config"
ALL_MODULE_JSON = "config/module.all"
LST_PUB_TYPE = ["pubdy3d"]
LST_PROJECT = ["MarsEditor", "DramaEditor", "UIEditor", "T2MapEditor"]


class CMainWidget(QtWidgets.QMainWindow, mainwidget.Ui_MainWindow):
    def __init__(self, *args):
        super(CMainWidget, self).__init__(*args)
        self.setupUi(self)
        self.m_PersonConfig = {}    #个人配置信息
        self.m_CommonConfig = {}    #通用配置信息
        self.m_AllModuleInfo = {}   #所有模块的所有版本信息
        self.m_ModuleVersion = {}   #当前模块对应的版本
        self.m_ModuleList = []      #[(模块名, 版本), ]
        self.InitConfig()
        self.InitUI()
        self.InitConnect()


    def InitConfig(self):
        self.m_PersonConfig = misc.JsonLoad(PERSON_CONFIG, {})
        self.m_CommonConfig = misc.JsonLoad(COMMON_CONFIG, {})
        

    def SaveConfig(self):
        sPubType = self.comboBoxPubType.currentText()
        sProject = self.comboBoxProject.currentText()

        self.m_PersonConfig["LastPubType"] = sPubType
        dPersonPubType = self.CreateInfo(self.m_PersonConfig, sPubType)
        dPersonPubType["LastProject"] = sProject
        dPersonProject = self.CreateInfo(dPersonPubType, sProject)
        dPersonProject["ScriptDir"] = self.lineEditScriptDir.text()

        dCommonPubType = self.CreateInfo(self.m_CommonConfig, sPubType)
        dCommonProject = self.CreateInfo(dCommonPubType, sProject)
        lstVersionRecord = self.CreateInfo(dCommonProject, "VersionRecord", [])
  
        sVersionName = self.lineEditVersionConfig.text()
        sVersionName = os.path.split(sVersionName)[1]
        sVersionName = os.path.splitext(sVersionName)[0]
        tInfo = (misc.Time2Str(), sVersionName)
        lstVersionRecord.append(tInfo)

        misc.JsonDump(self.m_PersonConfig, PERSON_CONFIG)
        misc.JsonDump(self.m_CommonConfig, COMMON_CONFIG)


    def InitUI(self):
        # lstPubType = self.m_CommonConfig.get("PubType", LST_PUB_TYPE)
        # lstProject = self.m_CommonConfig.get("PubType", LST_PROJECT)
        self.comboBoxPubType.addItems(LST_PUB_TYPE)
        self.comboBoxProject.addItems(LST_PROJECT)

        sLastType = self.m_PersonConfig.get("LastPubType", "")
        if sLastType:
            self.comboBoxPubType.setCurrentText(sLastType)
        sModuleFile = os.path.join("config", sLastType + ".module")
        self.m_AllModuleInfo = misc.JsonLoad(sModuleFile, {})

        dTypeInfo = self.m_PersonConfig.get(sLastType, {})
        sLastProject = dTypeInfo.get("LastProject", "")
        if sLastProject:
            self.comboBoxProject.setCurrentText(sLastProject)
        dProjectInfo = dTypeInfo.get(sLastProject, {})
        scriptDir = dProjectInfo.get("ScriptDir", os.getcwd())
        self.lineEditScriptDir.setText(scriptDir)

        self.InitModuleTreeWidget()


    def InitConnect(self):
        self.pushButtonVersionConfig.clicked.connect(self.ChooseVersionConfig)
        self.pushButtonScriptPath.clicked.connect(self.ChooseSciptPath)
        self.pushButtonExport.clicked.connect(self.ModuleExport)
        self.comboBoxPubType.currentTextChanged.connect(self.ChangePubType)
        self.comboBoxProject.currentTextChanged.connect(self.ChangeProject)


    def ChangePubType(self, sPubType):
        pass


    def ChangeProject(self, sProject):
        sPubType = self.comboBoxPubType.currentText()
        dTypeInfo = self.m_PersonConfig.get(sPubType, {})
        dProjectInfo = dTypeInfo.get(sProject, {})
        scriptDir = dProjectInfo.get("ScriptDir", os.getcwd())
        self.lineEditScriptDir.setText(scriptDir)

        
    def ChooseVersionConfig(self):
        """版本配置文件选择"""
        sFile = QtWidgets.QFileDialog.getOpenFileName(self, "版本配置文件选择", "", "Json文件(*.json)")[0]
        if not sFile:
            return
        self.m_ModuleVersion = {}
        self.m_ModuleList = []
        self.lineEditVersionConfig.setText(sFile)
        self.InitModuleTableWidget(sFile)
        self.ShowModuleTableWidget()


    def ChooseSciptPath(self):
        """选择脚本导出到那个路径"""
        sDir = QtWidgets.QFileDialog.getExistingDirectory(self, "脚本导出路径选择", "")
        if sDir:
            self.lineEditScriptDir.setText(sDir)


    def AddMoudleInfo(self, sModule, sVersion):
        if sModule in self.m_ModuleVersion:
            if self.m_ModuleVersion[sModule] != sVersion:
                print("%s存在两个版本有冲突:%s %s" % (sModule, sVersion, self.m_ModuleVersion[sModule]))
            return
        self.m_ModuleVersion[sModule] = sVersion


    def InitModuleTableWidget(self, sFile):
        """从配置读取版本信息，然后加载"""
        dModuleInfo = misc.JsonLoad(sFile, {})
        for sModule, dInfo in dModuleInfo.items():
            sVersion = dInfo["version"]
            self.AddMoudleInfo(sModule, sVersion)
            dRely = dInfo.get("rely", {})
            for key, value in dRely.items():
                self.AddMoudleInfo(key, value)


    def ShowModuleTableWidget(self):
        """显示已选择的模块+版本信息"""
        self.m_ModuleList = sorted(self.m_ModuleVersion.items(), key=lambda x:x[0])
        self.tableWidgetModule.clearContents()
        self.tableWidgetModule.setRowCount(len(self.m_ModuleList))
        self.tableWidgetModule.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        for iRow, lstInfo in enumerate(self.m_ModuleList):
            for iCol, value in enumerate(lstInfo):
                oItem = QtWidgets.QTableWidgetItem(value)
                oItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidgetModule.setItem(iRow, iCol, oItem)


    def CreateInfo(self, dInfo, key, defalult=None):
        """key不在dInfo中，用defalut值创建key，并返回"""
        if defalult is None:
            defalult = {}
        if not key in dInfo:
            dInfo[key] = defalult
        return dInfo[key]


    def ModuleExport(self):
        """模块导出"""
        sPubType = self.comboBoxPubType.currentText()
        destinationDir = os.path.join(self.lineEditScriptDir.text(), sPubType)
        # if not os.path.exists(destinationDir):
        #     os.makedirs(destinationDir)
        for (sModule, sVersion) in self.m_ModuleList:
            sourcePath = self.m_AllModuleInfo[sModule]["path"]
            sourceFile = os.path.join(sourcePath, sModule, sVersion)
            destinationFile = os.path.join(destinationDir, sModule, sVersion)
            print("source:", sourceFile)
            print("\t", destinationFile)

        self.SaveConfig()


    def InitModuleTreeWidget(self):
        """初始化模块树结构"""
        self.treeWidgetModule.clear()
        lstAllModule = sorted(self.m_AllModuleInfo.items(), key=lambda x:x[0])
        for (sModule, dVersion) in lstAllModule:
            oModuleTreeWidgetItem = QtWidgets.QTreeWidgetItem(self.treeWidgetModule, [sModule,])
            for sVersion in dVersion["version"]:
                QtWidgets.QTreeWidgetItem(oModuleTreeWidgetItem, [sVersion,])



def Show():
    app = QtWidgets.QApplication(sys.argv)
    obj = CMainWidget()
    obj.show()
    sys.exit(app.exec_())
