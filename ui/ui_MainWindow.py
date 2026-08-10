# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(886, 480)
        self.actionSeleziona_cartella = QAction(MainWindow)
        self.actionSeleziona_cartella.setObjectName(u"actionSeleziona_cartella")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.FolderNew))
        self.actionSeleziona_cartella.setIcon(icon)
        self.actionGuida = QAction(MainWindow)
        self.actionGuida.setObjectName(u"actionGuida")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.HelpFaq))
        self.actionGuida.setIcon(icon1)
        self.actionCrediti = QAction(MainWindow)
        self.actionCrediti.setObjectName(u"actionCrediti")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mainLayout = QVBoxLayout(self.centralwidget)
        self.mainLayout.setSpacing(16)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.folderPathName = QLabel(self.centralwidget)
        self.folderPathName.setObjectName(u"folderPathName")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folderPathName.sizePolicy().hasHeightForWidth())
        self.folderPathName.setSizePolicy(sizePolicy)
        self.folderPathName.setWordWrap(True)

        self.verticalLayout.addWidget(self.folderPathName)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.changeFolderButton = QToolButton(self.centralwidget)
        self.changeFolderButton.setObjectName(u"changeFolderButton")
        sizePolicy.setHeightForWidth(self.changeFolderButton.sizePolicy().hasHeightForWidth())
        self.changeFolderButton.setSizePolicy(sizePolicy)
        self.changeFolderButton.setIcon(icon)
        self.changeFolderButton.setAutoRepeatDelay(100)
        self.changeFolderButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.changeFolderButton.setArrowType(Qt.ArrowType.NoArrow)

        self.horizontalLayout.addWidget(self.changeFolderButton)

        self.updateDataButton = QToolButton(self.centralwidget)
        self.updateDataButton.setObjectName(u"updateDataButton")
        sizePolicy.setHeightForWidth(self.updateDataButton.sizePolicy().hasHeightForWidth())
        self.updateDataButton.setSizePolicy(sizePolicy)
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.updateDataButton.setIcon(icon2)
        self.updateDataButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.horizontalLayout.addWidget(self.updateDataButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_top = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.verticalLayout.addItem(self.verticalSpacer_top)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_6)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.statusTable = QTableWidget(self.centralwidget)
        self.statusTable.setObjectName(u"statusTable")
        self.statusTable.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.statusTable.sizePolicy().hasHeightForWidth())
        self.statusTable.setSizePolicy(sizePolicy1)
        self.statusTable.setAutoFillBackground(True)
        self.statusTable.setMidLineWidth(7)
        self.statusTable.setGridStyle(Qt.PenStyle.SolidLine)
        self.statusTable.setCornerButtonEnabled(False)
        self.statusTable.horizontalHeader().setVisible(True)
        self.statusTable.horizontalHeader().setCascadingSectionResizes(True)
        self.statusTable.horizontalHeader().setMinimumSectionSize(46)
        self.statusTable.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.statusTable.horizontalHeader().setStretchLastSection(True)
        self.statusTable.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.statusTable, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 0, 0, 1, 1)


        self.mainLayout.addLayout(self.gridLayout_2)

        self.modesLayout = QGridLayout()
        self.modesLayout.setSpacing(6)
        self.modesLayout.setObjectName(u"modesLayout")
        self.autoButton = QPushButton(self.centralwidget)
        self.autoButton.setObjectName(u"autoButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.autoButton.sizePolicy().hasHeightForWidth())
        self.autoButton.setSizePolicy(sizePolicy2)

        self.modesLayout.addWidget(self.autoButton, 0, 0, 1, 1)

        self.manualButton = QPushButton(self.centralwidget)
        self.manualButton.setObjectName(u"manualButton")
        sizePolicy2.setHeightForWidth(self.manualButton.sizePolicy().hasHeightForWidth())
        self.manualButton.setSizePolicy(sizePolicy2)

        self.modesLayout.addWidget(self.manualButton, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.modesLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.singleImgButton = QPushButton(self.centralwidget)
        self.singleImgButton.setObjectName(u"singleImgButton")
        sizePolicy2.setHeightForWidth(self.singleImgButton.sizePolicy().hasHeightForWidth())
        self.singleImgButton.setSizePolicy(sizePolicy2)

        self.modesLayout.addWidget(self.singleImgButton, 2, 0, 1, 1)

        self.hybridModeButton = QPushButton(self.centralwidget)
        self.hybridModeButton.setObjectName(u"hybridModeButton")
        sizePolicy2.setHeightForWidth(self.hybridModeButton.sizePolicy().hasHeightForWidth())
        self.hybridModeButton.setSizePolicy(sizePolicy2)

        self.modesLayout.addWidget(self.hybridModeButton, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.modesLayout.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)

        self.modesLayout.addItem(self.verticalSpacer_3, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.modesLayout.addItem(self.verticalSpacer_4, 1, 1, 1, 1)


        self.mainLayout.addLayout(self.modesLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 886, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSeleziona_cartella)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionGuida)
        self.menuHelp.addAction(self.actionCrediti)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PhotoClock", None))
        self.actionSeleziona_cartella.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.actionGuida.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionCrediti.setText(QCoreApplication.translate("MainWindow", u"Credits", None))
        self.folderPathName.setText(QCoreApplication.translate("MainWindow", u"Select the working folder", None))
        self.changeFolderButton.setText(QCoreApplication.translate("MainWindow", u"Change folder", None))
        self.updateDataButton.setText(QCoreApplication.translate("MainWindow", u"Refresh analysis", None))
        self.autoButton.setText(QCoreApplication.translate("MainWindow", u"Automatic mode", None))
        self.manualButton.setText(QCoreApplication.translate("MainWindow", u"Manual mode", None))
        self.singleImgButton.setText(QCoreApplication.translate("MainWindow", u"Single image mode", None))
        self.hybridModeButton.setText(QCoreApplication.translate("MainWindow", u"Hybrid mode", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

