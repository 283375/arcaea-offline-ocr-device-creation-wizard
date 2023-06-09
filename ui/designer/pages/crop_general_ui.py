# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crop_general.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from ui.implements.components.imageCropper import ImageCropper

class Ui_Crop_General(object):
    def setupUi(self, Crop_General):
        if not Crop_General.objectName():
            Crop_General.setObjectName(u"Crop_General")
        Crop_General.resize(594, 401)
        Crop_General.setWindowTitle(u"CropGeneral")
        self.verticalLayout = QVBoxLayout(Crop_General)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Crop_General)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.descLabel = QLabel(self.widget)
        self.descLabel.setObjectName(u"descLabel")

        self.horizontalLayout_2.addWidget(self.descLabel)

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.exampleImgLabel = QLabel(self.groupBox)
        self.exampleImgLabel.setObjectName(u"exampleImgLabel")
        self.exampleImgLabel.setStyleSheet(u"color: #9e9e9e;\n"
"font-style: italic;")

        self.horizontalLayout.addWidget(self.exampleImgLabel)


        self.horizontalLayout_2.addWidget(self.groupBox)


        self.verticalLayout.addWidget(self.widget)

        self.imageCropper = ImageCropper(Crop_General)
        self.imageCropper.setObjectName(u"imageCropper")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageCropper.sizePolicy().hasHeightForWidth())
        self.imageCropper.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.imageCropper)

        self.groupBox_2 = QGroupBox(Crop_General)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.resultLabel = QLabel(self.groupBox_2)
        self.resultLabel.setObjectName(u"resultLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.resultLabel.sizePolicy().hasHeightForWidth())
        self.resultLabel.setSizePolicy(sizePolicy1)
        self.resultLabel.setText(u"")

        self.horizontalLayout_3.addWidget(self.resultLabel)

        self.executeButton = QPushButton(self.groupBox_2)
        self.executeButton.setObjectName(u"executeButton")

        self.horizontalLayout_3.addWidget(self.executeButton)


        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(Crop_General)

        QMetaObject.connectSlotsByName(Crop_General)
    # setupUi

    def retranslateUi(self, Crop_General):
        self.descLabel.setText(QCoreApplication.translate("Crop_General", u"\u89e3\u91ca\u6587\u672c", None))
        self.groupBox.setTitle(QCoreApplication.translate("Crop_General", u"\u6837\u4f8b", None))
        self.exampleImgLabel.setText(QCoreApplication.translate("Crop_General", u"\u6837\u4f8b\u56fe\u7247", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Crop_General", u"\u7ed3\u679c", None))
        self.executeButton.setText(QCoreApplication.translate("Crop_General", u"\u8bc6\u522b", None))
        pass
    # retranslateUi

