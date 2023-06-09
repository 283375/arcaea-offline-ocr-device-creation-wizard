# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Welcome(object):
    def setupUi(self, Welcome):
        if not Welcome.objectName():
            Welcome.setObjectName(u"Welcome")
        Welcome.resize(550, 300)
        self.verticalLayout = QVBoxLayout(Welcome)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Welcome)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(Welcome)

        QMetaObject.connectSlotsByName(Welcome)
    # setupUi

    def retranslateUi(self, Welcome):
        Welcome.setWindowTitle(QCoreApplication.translate("Welcome", u"\u6b22\u8fce", None))
        self.label.setText(QCoreApplication.translate("Welcome", u"\u8981\u4f7f\u7528 arcaea-offline-ocr\uff0c\u4e00\u4e2a\u51c6\u786e\u7684\u8bbe\u5907\u5b9a\u4e49\u6587\u4ef6\u662f\u5fc5\u4e0d\u53ef\u5c11\u7684\u3002<br>\u672c\u5411\u5bfc\u5c06\u5f15\u5bfc\u60a8\u521b\u5efa\u4e00\u4e2a\u8bbe\u5907\u5b9a\u4e49\u6587\u4ef6\uff0c\u5355\u51fb\u53f3\u4e0b\u89d2\u7684\u201c\u524d\u8fdb\u201d\u6309\u94ae\u7ee7\u7eed\u3002", None))
    # retranslateUi

