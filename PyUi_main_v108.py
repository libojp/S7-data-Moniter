# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Ui_main_v108.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1483, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWid_data = QtWidgets.QTableWidget(self.tab)
        self.tableWid_data.setObjectName("tableWid_data")
        self.tableWid_data.setColumnCount(11)
        self.tableWid_data.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWid_data.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWid_data.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWid_data.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWid_data.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWid_data.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWid_data.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWid_data.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWid_data.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWid_data.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWid_data.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWid_data.setHorizontalHeaderItem(10, item)
        self.gridLayout_4.addWidget(self.tableWid_data, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget.setGeometry(QtCore.QRect(521, 1, 896, 682))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_foreWighing = QtWidgets.QLabel(self.layoutWidget)
        self.label_foreWighing.setObjectName("label_foreWighing")
        self.horizontalLayout_3.addWidget(self.label_foreWighing)
        spacerItem = QtWidgets.QSpacerItem(838, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.tableWidg_exWight = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidg_exWight.setObjectName("tableWidg_exWight")
        self.tableWidg_exWight.setColumnCount(10)
        self.tableWidg_exWight.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_exWight.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_exWight.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_exWight.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_exWight.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_exWight.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_exWight.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_exWight.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_exWight.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_exWight.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_exWight.setHorizontalHeaderItem(9, item)
        self.tableWidg_exWight.horizontalHeader().setDefaultSectionSize(80)
        self.gridLayout_5.addWidget(self.tableWidg_exWight, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_reWighing = QtWidgets.QLabel(self.layoutWidget)
        self.label_reWighing.setObjectName("label_reWighing")
        self.horizontalLayout_2.addWidget(self.label_reWighing)
        spacerItem1 = QtWidgets.QSpacerItem(838, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tableWidg_reWight = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidg_reWight.setObjectName("tableWidg_reWight")
        self.tableWidg_reWight.setColumnCount(10)
        self.tableWidg_reWight.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_reWight.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_reWight.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_reWight.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_reWight.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_reWight.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_reWight.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_reWight.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_reWight.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_reWight.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_reWight.setHorizontalHeaderItem(9, item)
        self.tableWidg_reWight.horizontalHeader().setDefaultSectionSize(80)
        self.verticalLayout_2.addWidget(self.tableWidg_reWight)
        self.gridLayout_7.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.gridLayout_8.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_result = QtWidgets.QLabel(self.layoutWidget)
        self.label_result.setObjectName("label_result")
        self.horizontalLayout.addWidget(self.label_result)
        spacerItem2 = QtWidgets.QSpacerItem(818, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.tableWidg_result = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidg_result.setObjectName("tableWidg_result")
        self.tableWidg_result.setColumnCount(10)
        self.tableWidg_result.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_result.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_result.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_result.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_result.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_result.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_result.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_result.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_result.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidg_result.setHorizontalHeaderItem(9, item)
        self.tableWidg_result.horizontalHeader().setDefaultSectionSize(80)
        self.verticalLayout_3.addWidget(self.tableWidg_result)
        self.gridLayout_8.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(140, 62, 191, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_total = QtWidgets.QLabel(self.layoutWidget1)
        self.label_total.setObjectName("label_total")
        self.gridLayout_3.addWidget(self.label_total, 0, 0, 1, 1)
        self.lineEd_total = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEd_total.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEd_total.setReadOnly(True)
        self.lineEd_total.setObjectName("lineEd_total")
        self.gridLayout_3.addWidget(self.lineEd_total, 0, 1, 1, 1)
        self.label_qualified = QtWidgets.QLabel(self.layoutWidget1)
        self.label_qualified.setObjectName("label_qualified")
        self.gridLayout_3.addWidget(self.label_qualified, 1, 0, 1, 1)
        self.lineEd_qualified = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEd_qualified.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEd_qualified.setReadOnly(True)
        self.lineEd_qualified.setObjectName("lineEd_qualified")
        self.gridLayout_3.addWidget(self.lineEd_qualified, 1, 1, 1, 1)
        self.label_addLiquid = QtWidgets.QLabel(self.layoutWidget1)
        self.label_addLiquid.setObjectName("label_addLiquid")
        self.gridLayout_3.addWidget(self.label_addLiquid, 2, 0, 1, 1)
        self.lineEd_addLiquid = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEd_addLiquid.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEd_addLiquid.setReadOnly(True)
        self.lineEd_addLiquid.setObjectName("lineEd_addLiquid")
        self.gridLayout_3.addWidget(self.lineEd_addLiquid, 2, 1, 1, 1)
        self.label_unqualified = QtWidgets.QLabel(self.layoutWidget1)
        self.label_unqualified.setObjectName("label_unqualified")
        self.gridLayout_3.addWidget(self.label_unqualified, 3, 0, 1, 1)
        self.lineEd_unqualified = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEd_unqualified.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEd_unqualified.setReadOnly(True)
        self.lineEd_unqualified.setObjectName("lineEd_unqualified")
        self.gridLayout_3.addWidget(self.lineEd_unqualified, 3, 1, 1, 1)
        self.label_qualifiedRate = QtWidgets.QLabel(self.layoutWidget1)
        self.label_qualifiedRate.setObjectName("label_qualifiedRate")
        self.gridLayout_3.addWidget(self.label_qualifiedRate, 4, 0, 1, 1)
        self.lineEd_qualifiedRate = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEd_qualifiedRate.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEd_qualifiedRate.setReadOnly(True)
        self.lineEd_qualifiedRate.setObjectName("lineEd_qualifiedRate")
        self.gridLayout_3.addWidget(self.lineEd_qualifiedRate, 4, 1, 1, 1)
        self.pushB_countClear = QtWidgets.QPushButton(self.tab_2)
        self.pushB_countClear.setGeometry(QtCore.QRect(170, 260, 131, 41))
        self.pushB_countClear.setObjectName("pushB_countClear")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 3, 1, 1)
        self.label_programName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_programName.setFont(font)
        self.label_programName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_programName.setObjectName("label_programName")
        self.gridLayout.addWidget(self.label_programName, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1483, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLogin = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/Icon/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogin.setIcon(icon)
        self.actionLogin.setObjectName("actionLogin")
        self.actionLogout = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/Icon/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogout.setIcon(icon1)
        self.actionLogout.setObjectName("actionLogout")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/Icon/Quit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon2)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionConnect_us = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/Icon/contact.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConnect_us.setIcon(icon3)
        self.actionConnect_us.setObjectName("actionConnect_us")
        self.actionConfig_Port = QtWidgets.QAction(MainWindow)
        self.actionConfig_Port.setObjectName("actionConfig_Port")
        self.actionData_Query = QtWidgets.QAction(MainWindow)
        self.actionData_Query.setObjectName("actionData_Query")
        self.menu.addAction(self.actionLogin)
        self.menu.addAction(self.actionLogout)
        self.menu.addSeparator()
        self.menu.addAction(self.actionQuit)
        self.menu_2.addAction(self.actionConfig_Port)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionData_Query)
        self.menu_3.addAction(self.actionAbout)
        self.menu_3.addAction(self.actionConnect_us)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWid_data.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序 号"))
        item = self.tableWid_data.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "料盘号"))
        item = self.tableWid_data.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "托盘中编号"))
        item = self.tableWid_data.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "记录时间"))
        item = self.tableWid_data.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "前称重"))
        item = self.tableWid_data.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "后称重"))
        item = self.tableWid_data.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "比较下限"))
        item = self.tableWid_data.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "比较上限"))
        item = self.tableWid_data.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "注液量"))
        item = self.tableWid_data.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "注液偏差"))
        item = self.tableWid_data.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "状态"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "数据表"))
        self.label_foreWighing.setText(_translate("MainWindow", "前称 ："))
        item = self.tableWidg_exWight.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidg_exWight.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidg_exWight.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidg_exWight.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidg_exWight.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidg_exWight.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidg_exWight.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidg_exWight.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidg_exWight.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidg_exWight.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        self.label_reWighing.setText(_translate("MainWindow", "后称 ："))
        item = self.tableWidg_reWight.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidg_reWight.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidg_reWight.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidg_reWight.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidg_reWight.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidg_reWight.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidg_reWight.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidg_reWight.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidg_reWight.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidg_reWight.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        self.label_result.setText(_translate("MainWindow", "当前结果 ："))
        item = self.tableWidg_result.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidg_result.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidg_result.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidg_result.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidg_result.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidg_result.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidg_result.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidg_result.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidg_result.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidg_result.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        self.label_total.setText(_translate("MainWindow", "总数："))
        self.label_qualified.setText(_translate("MainWindow", "合格数："))
        self.label_addLiquid.setText(_translate("MainWindow", "补液数："))
        self.label_unqualified.setText(_translate("MainWindow", "不良数："))
        self.label_qualifiedRate.setText(_translate("MainWindow", "合格率："))
        self.pushB_countClear.setText(_translate("MainWindow", "清 零"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "数据统计"))
        self.label_programName.setText(_translate("MainWindow", "电池称重数据显示"))
        self.menu.setTitle(_translate("MainWindow", "用户"))
        self.menu_2.setTitle(_translate("MainWindow", "配置"))
        self.menu_3.setTitle(_translate("MainWindow", "帮助"))
        self.actionLogin.setText(_translate("MainWindow", "登录"))
        self.actionLogout.setText(_translate("MainWindow", "注销"))
        self.actionQuit.setText(_translate("MainWindow", "退出"))
        self.actionAbout.setText(_translate("MainWindow", "关于"))
        self.actionConnect_us.setText(_translate("MainWindow", "联系我们"))
        self.actionConfig_Port.setText(_translate("MainWindow", "端口配置"))
        self.actionData_Query.setText(_translate("MainWindow", "数据查询"))

import image_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
