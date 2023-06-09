# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'introduction.ui'
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

class Ui_Introduction(object):
    def setupUi(self, Introduction):
        if not Introduction.objectName():
            Introduction.setObjectName(u"Introduction")
        Introduction.resize(500, 400)
        Introduction.setWindowTitle(u"Introduction")
        self.verticalLayout = QVBoxLayout(Introduction)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Introduction)
        self.label.setObjectName(u"label")
        self.label.setWindowTitle(u"Introduction")
        self.label.setText(u"Introduction text")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(Introduction)

        QMetaObject.connectSlotsByName(Introduction)
    # setupUi

    def retranslateUi(self, Introduction):
        pass
    # retranslateUi

