# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crop_introduction.ui'
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

class Ui_Crop_Introduction(object):
    def setupUi(self, Crop_Introduction):
        if not Crop_Introduction.objectName():
            Crop_Introduction.setObjectName(u"Crop_Introduction")
        Crop_Introduction.resize(500, 400)
        Crop_Introduction.setWindowTitle(u"CropIntroduction")
        self.verticalLayout = QVBoxLayout(Crop_Introduction)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Crop_Introduction)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.label)


        self.retranslateUi(Crop_Introduction)

        QMetaObject.connectSlotsByName(Crop_Introduction)
    # setupUi

    def retranslateUi(self, Crop_Introduction):
        self.label.setText(QCoreApplication.translate("Crop_Introduction", u"\u63a5\u4e0b\u6765\u5411\u5bfc\u5c06\u6307\u5f15\u60a8\u6846\u9009\u51fa\u56fe\u50cf\u8bc6\u522b\u533a\u57df\u3002\u5728\u6846\u9009\u65f6\uff0c\u8bf7\u6ce8\u610f\u4ee5\u4e0b\u7b80\u79f0\uff1a<br>\n"
"<ul>\n"
"  <li>\u4e0a\u4e0b\u5bf9\u9f50\uff1a\u6846\u9009\u8fb9\u7f18\u5e94\u7d27\u8d34\u6587\u5b57\u4e0a\u4e0b\u8fb9\u754c\uff08\u5de6\u53f3\u4e0d\u53d7\u6b64\u9650\u5236\uff09</li>\n"
"  <li>\u9002\u5f53\u7559\u767d\uff1a\u6846\u9009\u8fb9\u7f18\u53ef\u4e0e\u6587\u5b57\u7559\u51fa\u9002\u5f53\u8ddd\u79bb\uff0c\u4f46\u4e0d\u5e94\u5305\u542b\u5176\u5b83\u5143\u7d20</li>\n"
"</ul>\n"
"\u5728\u6846\u9009\u65f6\u8bf7\u6ce8\u610f\u6846\u9009\u5bbd\u5ea6\uff0c\u53ef\u968f\u65f6\u53c2\u8003\u53f3\u4e0a\u89d2\u7684\u6837\u4f8b\u56fe\u7247\u3002", None))
        pass
    # retranslateUi

