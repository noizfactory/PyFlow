# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:/GIT/nodes/PyFlow/GraphEditor_ui.ui'
#
# Created: Mon Jan 29 23:14:22 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1608, 875)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("AGraphPySide/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setSpacing(1)
        self.gridLayout_3.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontal_splitter = QtGui.QSplitter(self.centralwidget)
        self.horizontal_splitter.setStyleSheet("")
        self.horizontal_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.horizontal_splitter.setObjectName("horizontal_splitter")
        self.SceneWidget = QtGui.QWidget(self.horizontal_splitter)
        self.SceneWidget.setObjectName("SceneWidget")
        self.gridLayout = QtGui.QGridLayout(self.SceneWidget)
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.gridLayout.setObjectName("gridLayout")
        self.SceneLayout = QtGui.QGridLayout()
        self.SceneLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.SceneLayout.setContentsMargins(0, 0, 0, 0)
        self.SceneLayout.setObjectName("SceneLayout")
        self.gridLayout.addLayout(self.SceneLayout, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.horizontal_splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1608, 26))
        self.menuBar.setObjectName("menuBar")
        self.menuEdit = QtGui.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtGui.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuPlugins = QtGui.QMenu(self.menuBar)
        self.menuPlugins.setObjectName("menuPlugins")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.dockWidgetVariables = QtGui.QDockWidget(MainWindow)
        self.dockWidgetVariables.setMinimumSize(QtCore.QSize(150, 113))
        self.dockWidgetVariables.setFloating(False)
        self.dockWidgetVariables.setFeatures(QtGui.QDockWidget.AllDockWidgetFeatures)
        self.dockWidgetVariables.setObjectName("dockWidgetVariables")
        self.dockWidgetContents_5 = QtGui.QWidget()
        self.dockWidgetContents_5.setObjectName("dockWidgetContents_5")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_2 = QtGui.QScrollArea(self.dockWidgetContents_5)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 148, 756))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_5 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.leftDockGridLayout = QtGui.QGridLayout()
        self.leftDockGridLayout.setObjectName("leftDockGridLayout")
        self.gridLayout_5.addLayout(self.leftDockGridLayout, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea_2)
        self.dockWidgetVariables.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetVariables)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.dockWidgetNodeView = QtGui.QDockWidget(MainWindow)
        self.dockWidgetNodeView.setMinimumSize(QtCore.QSize(500, 166))
        self.dockWidgetNodeView.setAllowedAreas(QtCore.Qt.AllDockWidgetAreas)
        self.dockWidgetNodeView.setObjectName("dockWidgetNodeView")
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtGui.QScrollArea(self.dockWidgetContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_3 = QtGui.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 498, 594))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_4 = QtGui.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.gridLayout_4.addLayout(self.formLayout, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout.addWidget(self.scrollArea)
        self.dockWidgetNodeView.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetNodeView)
        self.dockWidgetUndoStack = QtGui.QDockWidget(MainWindow)
        self.dockWidgetUndoStack.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resources/history.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dockWidgetUndoStack.setWindowIcon(icon1)
        self.dockWidgetUndoStack.setObjectName("dockWidgetUndoStack")
        self.dockWidgetContents_3 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents_3.setSizePolicy(sizePolicy)
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.gridLayout_6 = QtGui.QGridLayout(self.dockWidgetContents_3)
        self.gridLayout_6.setSpacing(1)
        self.gridLayout_6.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.dockWidgetUndoStack.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetUndoStack)
        self.actionDelete = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/resources/delete_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon2)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSave = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/resources/save_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/resources/folder_open_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad.setIcon(icon4)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave_as = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/resources/save_as_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_as.setIcon(icon5)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionPlot_graph = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/resources/plot_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot_graph.setIcon(icon6)
        self.actionPlot_graph.setObjectName("actionPlot_graph")
        self.actionScreenshot = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/resources/screenshot_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScreenshot.setIcon(icon7)
        self.actionScreenshot.setObjectName("actionScreenshot")
        self.actionShortcuts = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/resources/shortcuts_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionShortcuts.setIcon(icon8)
        self.actionShortcuts.setObjectName("actionShortcuts")
        self.actionAlignLeft = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/resources/alignleft.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlignLeft.setIcon(icon9)
        self.actionAlignLeft.setObjectName("actionAlignLeft")
        self.actionAlignUp = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/resources/aligntop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlignUp.setIcon(icon10)
        self.actionAlignUp.setObjectName("actionAlignUp")
        self.actionPropertyView = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/resources/property_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPropertyView.setIcon(icon11)
        self.actionPropertyView.setObjectName("actionPropertyView")
        self.actionAlignBottom = QtGui.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/resources/alignbottom.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlignBottom.setIcon(icon12)
        self.actionAlignBottom.setObjectName("actionAlignBottom")
        self.actionAlignRight = QtGui.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/resources/alignright.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlignRight.setIcon(icon13)
        self.actionAlignRight.setObjectName("actionAlignRight")
        self.actionNew_Node = QtGui.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/resources/brick.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Node.setIcon(icon14)
        self.actionNew_Node.setObjectName("actionNew_Node")
        self.actionNew_Command = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/icons/resources/script.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNew_Command.setIcon(icon15)
        self.actionNew_Command.setObjectName("actionNew_Command")
        self.actionFunction_Library = QtGui.QAction(MainWindow)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/icons/resources/function.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFunction_Library.setIcon(icon16)
        self.actionFunction_Library.setObjectName("actionFunction_Library")
        self.actionClear_history = QtGui.QAction(MainWindow)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/icons/resources/clear_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear_history.setIcon(icon17)
        self.actionClear_history.setObjectName("actionClear_history")
        self.actionVariables = QtGui.QAction(MainWindow)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/icons/resources/variable.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionVariables.setIcon(icon18)
        self.actionVariables.setObjectName("actionVariables")
        self.actionHistory = QtGui.QAction(MainWindow)
        self.actionHistory.setIcon(icon1)
        self.actionHistory.setObjectName("actionHistory")
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionClear_history)
        self.menuView.addAction(self.actionVariables)
        self.menuView.addAction(self.actionHistory)
        self.menuView.addAction(self.actionPropertyView)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionSave_as)
        self.menuHelp.addAction(self.actionPlot_graph)
        self.menuHelp.addAction(self.actionShortcuts)
        self.menuPlugins.addAction(self.actionNew_Node)
        self.menuPlugins.addAction(self.actionNew_Command)
        self.menuPlugins.addAction(self.actionFunction_Library)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())
        self.menuBar.addAction(self.menuPlugins.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionPropertyView)
        self.toolBar.addAction(self.actionVariables)
        self.toolBar.addAction(self.actionHistory)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionPlot_graph)
        self.toolBar.addAction(self.actionScreenshot)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAlignLeft)
        self.toolBar.addAction(self.actionAlignUp)
        self.toolBar.addAction(self.actionAlignBottom)
        self.toolBar.addAction(self.actionAlignRight)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyFlow", None, QtGui.QApplication.UnicodeUTF8))
        self.menuEdit.setTitle(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPlugins.setTitle(QtGui.QApplication.translate("MainWindow", "Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetVariables.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Variables", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetNodeView.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PropertyView", None, QtGui.QApplication.UnicodeUTF8))
        self.dockWidgetUndoStack.setWindowTitle(QtGui.QApplication.translate("MainWindow", "History", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_as.setText(QtGui.QApplication.translate("MainWindow", "Save as", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlot_graph.setText(QtGui.QApplication.translate("MainWindow", "Plot graph", None, QtGui.QApplication.UnicodeUTF8))
        self.actionScreenshot.setText(QtGui.QApplication.translate("MainWindow", "Screenshot", None, QtGui.QApplication.UnicodeUTF8))
        self.actionShortcuts.setText(QtGui.QApplication.translate("MainWindow", "Shortcuts", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlignLeft.setText(QtGui.QApplication.translate("MainWindow", "AlignLeft", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlignLeft.setToolTip(QtGui.QApplication.translate("MainWindow", "Align selected nodes by the left most", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlignUp.setText(QtGui.QApplication.translate("MainWindow", "AlignUp", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlignUp.setToolTip(QtGui.QApplication.translate("MainWindow", "Align selected nodes by the up most", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPropertyView.setText(QtGui.QApplication.translate("MainWindow", "PropertyView", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPropertyView.setToolTip(QtGui.QApplication.translate("MainWindow", "toggle property view", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlignBottom.setText(QtGui.QApplication.translate("MainWindow", "AlignBottom", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAlignRight.setText(QtGui.QApplication.translate("MainWindow", "alignRight", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Node.setText(QtGui.QApplication.translate("MainWindow", "New node", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Node.setToolTip(QtGui.QApplication.translate("MainWindow", "New node", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Command.setText(QtGui.QApplication.translate("MainWindow", "New editor command", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Command.setToolTip(QtGui.QApplication.translate("MainWindow", "New editor command", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFunction_Library.setText(QtGui.QApplication.translate("MainWindow", "New function library", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFunction_Library.setToolTip(QtGui.QApplication.translate("MainWindow", "New function library", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClear_history.setText(QtGui.QApplication.translate("MainWindow", "Clear history", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVariables.setText(QtGui.QApplication.translate("MainWindow", "Variables", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHistory.setText(QtGui.QApplication.translate("MainWindow", "History", None, QtGui.QApplication.UnicodeUTF8))

import nodes_res_rc
