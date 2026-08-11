# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manual_date_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QDialog, QFrame,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_ManualDateDialog(object):
    def setupUi(self, ManualDateDialog):
        if not ManualDateDialog.objectName():
            ManualDateDialog.setObjectName(u"ManualDateDialog")
        ManualDateDialog.resize(540, 500)
        ManualDateDialog.setModal(True)
        ManualDateDialog.setSizeGripEnabled(True)
        self.mainLayout = QVBoxLayout(ManualDateDialog)
        self.mainLayout.setSpacing(14)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(20, 20, 20, 20)
        self.imagePreview = QLabel(ManualDateDialog)
        self.imagePreview.setObjectName(u"imagePreview")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.imagePreview.sizePolicy().hasHeightForWidth())
        self.imagePreview.setSizePolicy(sizePolicy)
        self.imagePreview.setMinimumSize(QSize(200, 150))
        self.imagePreview.setFrameShape(QFrame.Shape.Box)
        self.imagePreview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.imagePreview.setScaledContents(False)

        self.mainLayout.addWidget(self.imagePreview)

        self.fileNameLabel = QLabel(ManualDateDialog)
        self.fileNameLabel.setObjectName(u"fileNameLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fileNameLabel.sizePolicy().hasHeightForWidth())
        self.fileNameLabel.setSizePolicy(sizePolicy1)
        self.fileNameLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fileNameLabel.setWordWrap(True)

        self.mainLayout.addWidget(self.fileNameLabel)

        self.dateLayout = QHBoxLayout()
        self.dateLayout.setObjectName(u"dateLayout")
        self.dateLabel = QLabel(ManualDateDialog)
        self.dateLabel.setObjectName(u"dateLabel")

        self.dateLayout.addWidget(self.dateLabel)

        self.dateTimeEdit = QDateTimeEdit(ManualDateDialog)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dateTimeEdit.sizePolicy().hasHeightForWidth())
        self.dateTimeEdit.setSizePolicy(sizePolicy2)
        self.dateTimeEdit.setCalendarPopup(True)

        self.dateLayout.addWidget(self.dateTimeEdit)


        self.mainLayout.addLayout(self.dateLayout)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.abortButton = QPushButton(ManualDateDialog)
        self.abortButton.setObjectName(u"abortButton")

        self.buttonLayout.addWidget(self.abortButton)

        self.skipButton = QPushButton(ManualDateDialog)
        self.skipButton.setObjectName(u"skipButton")

        self.buttonLayout.addWidget(self.skipButton)

        self.buttonSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.buttonSpacer)

        self.confirmButton = QPushButton(ManualDateDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.buttonLayout.addWidget(self.confirmButton)


        self.mainLayout.addLayout(self.buttonLayout)


        self.retranslateUi(ManualDateDialog)

        self.confirmButton.setDefault(True)


        QMetaObject.connectSlotsByName(ManualDateDialog)
    # setupUi

    def retranslateUi(self, ManualDateDialog):
        ManualDateDialog.setWindowTitle(QCoreApplication.translate("ManualDateDialog", u"Enter image date", None))
        self.imagePreview.setText("")
        self.fileNameLabel.setText(QCoreApplication.translate("ManualDateDialog", u"file_name.jpg", None))
        self.dateLabel.setText(QCoreApplication.translate("ManualDateDialog", u"Date:", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("ManualDateDialog", u"yyyy:MM:dd HH:mm:ss", None))
        self.abortButton.setText(QCoreApplication.translate("ManualDateDialog", u"Abort", None))
        self.skipButton.setText(QCoreApplication.translate("ManualDateDialog", u"Skip", None))
        self.confirmButton.setText(QCoreApplication.translate("ManualDateDialog", u"Confirm", None))
    # retranslateUi

