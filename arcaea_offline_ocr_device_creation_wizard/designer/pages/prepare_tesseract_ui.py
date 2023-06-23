# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prepare_tesseract.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from ...implements.components.fileSelector import FileSelector

class Ui_Prepare_Tesseract(object):
    def setupUi(self, Prepare_Tesseract):
        if not Prepare_Tesseract.objectName():
            Prepare_Tesseract.setObjectName(u"Prepare_Tesseract")
        Prepare_Tesseract.resize(500, 400)
        Prepare_Tesseract.setWindowTitle(u"Prepare Tesseract")
        self.verticalLayout = QVBoxLayout(Prepare_Tesseract)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Prepare_Tesseract)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Prepare_Tesseract)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.groupBox_3 = QGroupBox(Prepare_Tesseract)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.imageLabel = QLabel(self.groupBox_3)
        self.imageLabel.setObjectName(u"imageLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setText(u"")
        self.imageLabel.setPixmap(QPixmap(u":/images/ocr_test.png"))
        self.imageLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.imageLabel)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(Prepare_Tesseract)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy1)
        self.label_4.setText(u"tesseract")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.tesseractFileSelector = FileSelector(self.groupBox)
        self.tesseractFileSelector.setObjectName(u"tesseractFileSelector")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.tesseractFileSelector)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        sizePolicy1.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy1)
        self.label_5.setText(u"tessdata")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.widget_2 = QWidget(self.groupBox)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tessdataAutoCheckBox = QCheckBox(self.widget_2)
        self.tessdataAutoCheckBox.setObjectName(u"tessdataAutoCheckBox")

        self.horizontalLayout.addWidget(self.tessdataAutoCheckBox)

        self.tessdataFileSelector = FileSelector(self.widget_2)
        self.tessdataFileSelector.setObjectName(u"tessdataFileSelector")
        sizePolicy.setHeightForWidth(self.tessdataFileSelector.sizePolicy().hasHeightForWidth())
        self.tessdataFileSelector.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.tessdataFileSelector)


        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.widget_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Prepare_Tesseract)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.resultLabel = QLabel(self.groupBox_2)
        self.resultLabel.setObjectName(u"resultLabel")
        sizePolicy.setHeightForWidth(self.resultLabel.sizePolicy().hasHeightForWidth())
        self.resultLabel.setSizePolicy(sizePolicy)
        self.resultLabel.setText(u"")

        self.horizontalLayout_3.addWidget(self.resultLabel)

        self.executeButton = QPushButton(self.groupBox_2)
        self.executeButton.setObjectName(u"executeButton")

        self.horizontalLayout_3.addWidget(self.executeButton)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Prepare_Tesseract)

        QMetaObject.connectSlotsByName(Prepare_Tesseract)
    # setupUi

    def retranslateUi(self, Prepare_Tesseract):
        self.label.setText(QCoreApplication.translate("Prepare_Tesseract", u"\u63a5\u4e0b\u6765\u9a8c\u8bc1 OCR \u5f15\u64ce\uff08tesseract\uff09\u662f\u5426\u6b63\u5e38\u5de5\u4f5c\u3002", None))
        self.label_2.setText(QCoreApplication.translate("Prepare_Tesseract", u"\u8bf7\u5728\u914d\u7f6e tesseract \u540e\u6309\u4e0b\u201c\u68c0\u6d4b\u201d\u6309\u94ae\uff0c\u786e\u8ba4\u8bc6\u522b\u7ed3\u679c\u4e0e\u56fe\u7247\u65e0\u8bef\u540e\u7ee7\u7eed\u3002", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Prepare_Tesseract", u"\u8f93\u5165", None))
        self.groupBox.setTitle(QCoreApplication.translate("Prepare_Tesseract", u"\u914d\u7f6e", None))
        self.tessdataAutoCheckBox.setText(QCoreApplication.translate("Prepare_Tesseract", u"\u81ea\u52a8", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Prepare_Tesseract", u"\u8f93\u51fa", None))
        self.executeButton.setText(QCoreApplication.translate("Prepare_Tesseract", u"\u68c0\u6d4b", None))
        pass
    # retranslateUi

