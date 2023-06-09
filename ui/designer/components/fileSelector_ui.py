# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fileSelector.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)

from ui.extends.elidedLabel import ElidedLabel

class Ui_FileSelector(object):
    def setupUi(self, FileSelector):
        if not FileSelector.objectName():
            FileSelector.setObjectName(u"FileSelector")
        FileSelector.resize(500, 80)
        FileSelector.setWindowTitle(u"FileSelector")
        self.horizontalLayout = QHBoxLayout(FileSelector)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.elidedLabel = ElidedLabel(FileSelector)
        self.elidedLabel.setObjectName(u"elidedLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.elidedLabel.sizePolicy().hasHeightForWidth())
        self.elidedLabel.setSizePolicy(sizePolicy)
        self.elidedLabel.setText(u"...")

        self.horizontalLayout.addWidget(self.elidedLabel)

        self.pushButton = QPushButton(FileSelector)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)


        self.retranslateUi(FileSelector)

        QMetaObject.connectSlotsByName(FileSelector)
    # setupUi

    def retranslateUi(self, FileSelector):
        self.pushButton.setText(QCoreApplication.translate("FileSelector", u"\u9009\u62e9", None))
        pass
    # retranslateUi

