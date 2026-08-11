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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(980, 640)
        MainWindow.setMinimumSize(QSize(760, 520))
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
        self.mainLayout.setSpacing(18)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(24, 20, 24, 24)
        self.headerCard = QFrame(self.centralwidget)
        self.headerCard.setObjectName(u"headerCard")
        self.headerCard.setFrameShape(QFrame.Shape.NoFrame)
        self.headerCardLayout = QHBoxLayout(self.headerCard)
        self.headerCardLayout.setSpacing(14)
        self.headerCardLayout.setObjectName(u"headerCardLayout")
        self.headerCardLayout.setContentsMargins(18, 14, 18, 14)
        self.folderIconLabel = QLabel(self.headerCard)
        self.folderIconLabel.setObjectName(u"folderIconLabel")

        self.headerCardLayout.addWidget(self.folderIconLabel)

        self.folderTextLayout = QVBoxLayout()
        self.folderTextLayout.setSpacing(2)
        self.folderTextLayout.setObjectName(u"folderTextLayout")
        self.folderCaption = QLabel(self.headerCard)
        self.folderCaption.setObjectName(u"folderCaption")

        self.folderTextLayout.addWidget(self.folderCaption)

        self.folderPathName = QLabel(self.headerCard)
        self.folderPathName.setObjectName(u"folderPathName")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folderPathName.sizePolicy().hasHeightForWidth())
        self.folderPathName.setSizePolicy(sizePolicy)
        self.folderPathName.setWordWrap(True)

        self.folderTextLayout.addWidget(self.folderPathName)


        self.headerCardLayout.addLayout(self.folderTextLayout)

        self.headerSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.headerCardLayout.addItem(self.headerSpacer)

        self.changeFolderButton = QToolButton(self.headerCard)
        self.changeFolderButton.setObjectName(u"changeFolderButton")
        self.changeFolderButton.setIcon(icon)
        self.changeFolderButton.setAutoRepeatDelay(100)
        self.changeFolderButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.changeFolderButton.setArrowType(Qt.ArrowType.NoArrow)

        self.headerCardLayout.addWidget(self.changeFolderButton)

        self.updateDataButton = QToolButton(self.headerCard)
        self.updateDataButton.setObjectName(u"updateDataButton")
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ViewRefresh))
        self.updateDataButton.setIcon(icon2)
        self.updateDataButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)

        self.headerCardLayout.addWidget(self.updateDataButton)


        self.mainLayout.addWidget(self.headerCard)

        self.statsRow = QHBoxLayout()
        self.statsRow.setSpacing(14)
        self.statsRow.setObjectName(u"statsRow")
        self.statCardImages = QFrame(self.centralwidget)
        self.statCardImages.setObjectName(u"statCardImages")
        self.statCardImages.setMinimumSize(QSize(0, 78))
        self.statCardImages.setFrameShape(QFrame.Shape.NoFrame)
        self.statCardImagesLayout = QVBoxLayout(self.statCardImages)
        self.statCardImagesLayout.setSpacing(4)
        self.statCardImagesLayout.setObjectName(u"statCardImagesLayout")
        self.statCardImagesLayout.setContentsMargins(16, 12, 16, 12)
        self.statValueImages = QLabel(self.statCardImages)
        self.statValueImages.setObjectName(u"statValueImages")

        self.statCardImagesLayout.addWidget(self.statValueImages)

        self.statCaptionImages = QLabel(self.statCardImages)
        self.statCaptionImages.setObjectName(u"statCaptionImages")
        self.statCaptionImages.setWordWrap(True)

        self.statCardImagesLayout.addWidget(self.statCaptionImages)


        self.statsRow.addWidget(self.statCardImages)

        self.statCardNoData = QFrame(self.centralwidget)
        self.statCardNoData.setObjectName(u"statCardNoData")
        self.statCardNoData.setMinimumSize(QSize(0, 78))
        self.statCardNoData.setFrameShape(QFrame.Shape.NoFrame)
        self.statCardNoDataLayout = QVBoxLayout(self.statCardNoData)
        self.statCardNoDataLayout.setSpacing(4)
        self.statCardNoDataLayout.setObjectName(u"statCardNoDataLayout")
        self.statCardNoDataLayout.setContentsMargins(16, 12, 16, 12)
        self.statValueNoData = QLabel(self.statCardNoData)
        self.statValueNoData.setObjectName(u"statValueNoData")

        self.statCardNoDataLayout.addWidget(self.statValueNoData)

        self.statCaptionNoData = QLabel(self.statCardNoData)
        self.statCaptionNoData.setObjectName(u"statCaptionNoData")
        self.statCaptionNoData.setWordWrap(True)

        self.statCardNoDataLayout.addWidget(self.statCaptionNoData)


        self.statsRow.addWidget(self.statCardNoData)

        self.statCardFixedAuto = QFrame(self.centralwidget)
        self.statCardFixedAuto.setObjectName(u"statCardFixedAuto")
        self.statCardFixedAuto.setMinimumSize(QSize(0, 78))
        self.statCardFixedAuto.setFrameShape(QFrame.Shape.NoFrame)
        self.statCardFixedAutoLayout = QVBoxLayout(self.statCardFixedAuto)
        self.statCardFixedAutoLayout.setSpacing(4)
        self.statCardFixedAutoLayout.setObjectName(u"statCardFixedAutoLayout")
        self.statCardFixedAutoLayout.setContentsMargins(16, 12, 16, 12)
        self.statValueFixedAuto = QLabel(self.statCardFixedAuto)
        self.statValueFixedAuto.setObjectName(u"statValueFixedAuto")

        self.statCardFixedAutoLayout.addWidget(self.statValueFixedAuto)

        self.statCaptionFixedAuto = QLabel(self.statCardFixedAuto)
        self.statCaptionFixedAuto.setObjectName(u"statCaptionFixedAuto")
        self.statCaptionFixedAuto.setWordWrap(True)

        self.statCardFixedAutoLayout.addWidget(self.statCaptionFixedAuto)


        self.statsRow.addWidget(self.statCardFixedAuto)

        self.statCardFixedManual = QFrame(self.centralwidget)
        self.statCardFixedManual.setObjectName(u"statCardFixedManual")
        self.statCardFixedManual.setMinimumSize(QSize(0, 78))
        self.statCardFixedManual.setFrameShape(QFrame.Shape.NoFrame)
        self.statCardFixedManualLayout = QVBoxLayout(self.statCardFixedManual)
        self.statCardFixedManualLayout.setSpacing(4)
        self.statCardFixedManualLayout.setObjectName(u"statCardFixedManualLayout")
        self.statCardFixedManualLayout.setContentsMargins(16, 12, 16, 12)
        self.statValueFixedManual = QLabel(self.statCardFixedManual)
        self.statValueFixedManual.setObjectName(u"statValueFixedManual")

        self.statCardFixedManualLayout.addWidget(self.statValueFixedManual)

        self.statCaptionFixedManual = QLabel(self.statCardFixedManual)
        self.statCaptionFixedManual.setObjectName(u"statCaptionFixedManual")
        self.statCaptionFixedManual.setWordWrap(True)

        self.statCardFixedManualLayout.addWidget(self.statCaptionFixedManual)


        self.statsRow.addWidget(self.statCardFixedManual)

        self.statCardSkipped = QFrame(self.centralwidget)
        self.statCardSkipped.setObjectName(u"statCardSkipped")
        self.statCardSkipped.setMinimumSize(QSize(0, 78))
        self.statCardSkipped.setFrameShape(QFrame.Shape.NoFrame)
        self.statCardSkippedLayout = QVBoxLayout(self.statCardSkipped)
        self.statCardSkippedLayout.setSpacing(4)
        self.statCardSkippedLayout.setObjectName(u"statCardSkippedLayout")
        self.statCardSkippedLayout.setContentsMargins(16, 12, 16, 12)
        self.statValueSkipped = QLabel(self.statCardSkipped)
        self.statValueSkipped.setObjectName(u"statValueSkipped")

        self.statCardSkippedLayout.addWidget(self.statValueSkipped)

        self.statCaptionSkipped = QLabel(self.statCardSkipped)
        self.statCaptionSkipped.setObjectName(u"statCaptionSkipped")
        self.statCaptionSkipped.setWordWrap(True)

        self.statCardSkippedLayout.addWidget(self.statCaptionSkipped)


        self.statsRow.addWidget(self.statCardSkipped)


        self.mainLayout.addLayout(self.statsRow)

        self.modesLayout = QGridLayout()
        self.modesLayout.setSpacing(14)
        self.modesLayout.setObjectName(u"modesLayout")
        self.autoTileLayout = QVBoxLayout()
        self.autoTileLayout.setSpacing(6)
        self.autoTileLayout.setObjectName(u"autoTileLayout")
        self.autoButton = QPushButton(self.centralwidget)
        self.autoButton.setObjectName(u"autoButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.autoButton.sizePolicy().hasHeightForWidth())
        self.autoButton.setSizePolicy(sizePolicy1)
        self.autoButton.setMinimumSize(QSize(0, 84))
        self.autoButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.autoTileLayout.addWidget(self.autoButton)

        self.autoCaption = QLabel(self.centralwidget)
        self.autoCaption.setObjectName(u"autoCaption")
        self.autoCaption.setWordWrap(True)

        self.autoTileLayout.addWidget(self.autoCaption)


        self.modesLayout.addLayout(self.autoTileLayout, 0, 0, 1, 1)

        self.manualTileLayout = QVBoxLayout()
        self.manualTileLayout.setSpacing(6)
        self.manualTileLayout.setObjectName(u"manualTileLayout")
        self.manualButton = QPushButton(self.centralwidget)
        self.manualButton.setObjectName(u"manualButton")
        sizePolicy1.setHeightForWidth(self.manualButton.sizePolicy().hasHeightForWidth())
        self.manualButton.setSizePolicy(sizePolicy1)
        self.manualButton.setMinimumSize(QSize(0, 84))
        self.manualButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.manualTileLayout.addWidget(self.manualButton)

        self.manualCaption = QLabel(self.centralwidget)
        self.manualCaption.setObjectName(u"manualCaption")
        self.manualCaption.setWordWrap(True)

        self.manualTileLayout.addWidget(self.manualCaption)


        self.modesLayout.addLayout(self.manualTileLayout, 0, 1, 1, 1)

        self.singleImgTileLayout = QVBoxLayout()
        self.singleImgTileLayout.setSpacing(6)
        self.singleImgTileLayout.setObjectName(u"singleImgTileLayout")
        self.singleImgButton = QPushButton(self.centralwidget)
        self.singleImgButton.setObjectName(u"singleImgButton")
        sizePolicy1.setHeightForWidth(self.singleImgButton.sizePolicy().hasHeightForWidth())
        self.singleImgButton.setSizePolicy(sizePolicy1)
        self.singleImgButton.setMinimumSize(QSize(0, 84))
        self.singleImgButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.singleImgTileLayout.addWidget(self.singleImgButton)

        self.singleImgCaption = QLabel(self.centralwidget)
        self.singleImgCaption.setObjectName(u"singleImgCaption")
        self.singleImgCaption.setWordWrap(True)

        self.singleImgTileLayout.addWidget(self.singleImgCaption)


        self.modesLayout.addLayout(self.singleImgTileLayout, 1, 0, 1, 1)

        self.hybridTileLayout = QVBoxLayout()
        self.hybridTileLayout.setSpacing(6)
        self.hybridTileLayout.setObjectName(u"hybridTileLayout")
        self.hybridModeButton = QPushButton(self.centralwidget)
        self.hybridModeButton.setObjectName(u"hybridModeButton")
        sizePolicy1.setHeightForWidth(self.hybridModeButton.sizePolicy().hasHeightForWidth())
        self.hybridModeButton.setSizePolicy(sizePolicy1)
        self.hybridModeButton.setMinimumSize(QSize(0, 84))
        self.hybridModeButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.hybridTileLayout.addWidget(self.hybridModeButton)

        self.hybridCaption = QLabel(self.centralwidget)
        self.hybridCaption.setObjectName(u"hybridCaption")
        self.hybridCaption.setWordWrap(True)

        self.hybridTileLayout.addWidget(self.hybridCaption)


        self.modesLayout.addLayout(self.hybridTileLayout, 1, 1, 1, 1)


        self.mainLayout.addLayout(self.modesLayout)

        self.mainLayout.setStretch(2, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 980, 26))
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PicMetadata", None))
        self.actionSeleziona_cartella.setText(QCoreApplication.translate("MainWindow", u"Select folder", None))
        self.actionGuida.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.actionCrediti.setText(QCoreApplication.translate("MainWindow", u"Credits", None))
        self.folderIconLabel.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c1", None))
        self.folderCaption.setText(QCoreApplication.translate("MainWindow", u"Working folder", None))
        self.folderPathName.setText(QCoreApplication.translate("MainWindow", u"Select the working folder", None))
        self.changeFolderButton.setText(QCoreApplication.translate("MainWindow", u"Change folder", None))
        self.updateDataButton.setText(QCoreApplication.translate("MainWindow", u"Refresh analysis", None))
        self.statCardImages.setProperty(u"accent", QCoreApplication.translate("MainWindow", u"brand", None))
        self.statValueImages.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.statCaptionImages.setText(QCoreApplication.translate("MainWindow", u"Number of images", None))
        self.statCardNoData.setProperty(u"accent", QCoreApplication.translate("MainWindow", u"warning", None))
        self.statValueNoData.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.statCaptionNoData.setText(QCoreApplication.translate("MainWindow", u"Images without a date", None))
        self.statCardFixedAuto.setProperty(u"accent", QCoreApplication.translate("MainWindow", u"success", None))
        self.statValueFixedAuto.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.statCaptionFixedAuto.setText(QCoreApplication.translate("MainWindow", u"Fixed automatically", None))
        self.statCardFixedManual.setProperty(u"accent", QCoreApplication.translate("MainWindow", u"info", None))
        self.statValueFixedManual.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.statCaptionFixedManual.setText(QCoreApplication.translate("MainWindow", u"Fixed manually", None))
        self.statCardSkipped.setProperty(u"accent", QCoreApplication.translate("MainWindow", u"neutral", None))
        self.statValueSkipped.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.statCaptionSkipped.setText(QCoreApplication.translate("MainWindow", u"Skipped", None))
        self.autoButton.setText(QCoreApplication.translate("MainWindow", u"Automatic mode", None))
        self.autoCaption.setText(QCoreApplication.translate("MainWindow", u"Fix dates for images whose filename already contains a recognizable date.", None))
        self.manualButton.setText(QCoreApplication.translate("MainWindow", u"Manual mode", None))
        self.manualCaption.setText(QCoreApplication.translate("MainWindow", u"Review every image without a date and set it by hand.", None))
        self.singleImgButton.setText(QCoreApplication.translate("MainWindow", u"Single image mode", None))
        self.singleImgCaption.setText(QCoreApplication.translate("MainWindow", u"Pick one or more images yourself and set their date.", None))
        self.hybridModeButton.setText(QCoreApplication.translate("MainWindow", u"Hybrid mode", None))
        self.hybridCaption.setText(QCoreApplication.translate("MainWindow", u"Automatic first, then asks manually for the rest.", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

