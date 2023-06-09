# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crop_selectScreenshot.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

from ui.implements.components.fileSelector import FileSelector

class Ui_Crop_SelectScreenshot(object):
    def setupUi(self, Crop_SelectScreenshot):
        if not Crop_SelectScreenshot.objectName():
            Crop_SelectScreenshot.setObjectName(u"Crop_SelectScreenshot")
        Crop_SelectScreenshot.resize(500, 400)
        self.verticalLayout = QVBoxLayout(Crop_SelectScreenshot)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Crop_SelectScreenshot)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.graphicsView = QGraphicsView(Crop_SelectScreenshot)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout.addWidget(self.graphicsView)

        self.fileSelector = FileSelector(Crop_SelectScreenshot)
        self.fileSelector.setObjectName(u"fileSelector")

        self.verticalLayout.addWidget(self.fileSelector)


        self.retranslateUi(Crop_SelectScreenshot)

        QMetaObject.connectSlotsByName(Crop_SelectScreenshot)
    # setupUi

    def retranslateUi(self, Crop_SelectScreenshot):
        Crop_SelectScreenshot.setWindowTitle(QCoreApplication.translate("Crop_SelectScreenshot", u"Form", None))
        self.label.setText(QCoreApplication.translate("Crop_SelectScreenshot", u"\u9996\u5148\uff0c\u8bf7\u9009\u62e9\u60a8\u8bbe\u5907\u7684\u4e00\u5f20 Arcaea \u6210\u7ee9\u622a\u56fe\u3002", None))
    # retranslateUi

