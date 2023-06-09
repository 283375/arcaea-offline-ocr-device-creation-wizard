# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'prepare_arcaeaOfflineOcr.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Prepare_ArcaeaOfflineOcr(object):
    def setupUi(self, PrepareArcaeaOfflineOcr):
        if not PrepareArcaeaOfflineOcr.objectName():
            PrepareArcaeaOfflineOcr.setObjectName(u"PrepareArcaeaOfflineOcr")
        PrepareArcaeaOfflineOcr.resize(450, 300)
        PrepareArcaeaOfflineOcr.setWindowTitle(u"Prepare arcaea_offline_ocr")
        self.verticalLayout = QVBoxLayout(PrepareArcaeaOfflineOcr)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(PrepareArcaeaOfflineOcr)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.groupBox = QGroupBox(PrepareArcaeaOfflineOcr)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText(u"importlib.metadata.version(\"arcaea-offline-ocr\")")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox1 = QGroupBox(PrepareArcaeaOfflineOcr)
        self.groupBox1.setObjectName(u"groupBox1")
        self.horizontalLayout = QHBoxLayout(self.groupBox1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.resultLabel = QLabel(self.groupBox1)
        self.resultLabel.setObjectName(u"resultLabel")
        sizePolicy.setHeightForWidth(self.resultLabel.sizePolicy().hasHeightForWidth())
        self.resultLabel.setSizePolicy(sizePolicy)
        self.resultLabel.setText(u"")

        self.horizontalLayout.addWidget(self.resultLabel)

        self.executeButton = QPushButton(self.groupBox1)
        self.executeButton.setObjectName(u"executeButton")

        self.horizontalLayout.addWidget(self.executeButton)


        self.verticalLayout.addWidget(self.groupBox1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(PrepareArcaeaOfflineOcr)

        QMetaObject.connectSlotsByName(PrepareArcaeaOfflineOcr)
    # setupUi

    def retranslateUi(self, PrepareArcaeaOfflineOcr):
        self.label_2.setText(QCoreApplication.translate("Prepare_ArcaeaOfflineOcr", u"\u73b0\u5728\u68c0\u6d4b arcaea-offline-ocr \u662f\u5426\u6b63\u5e38\u5bfc\u5165\u3002<br>\n"
"\u8bf7\u786e\u4fdd\u201c\u7ed3\u679c\u201d\u7a97\u53e3\u4e2d\u6709\u6709\u6548\u7248\u672c\u53f7\u8f93\u51fa\u3002<br>\n"
"\uff08\u793a\u4f8b\uff1a0.1.0\uff09", None))
        self.groupBox.setTitle(QCoreApplication.translate("Prepare_ArcaeaOfflineOcr", u"\u8f93\u5165", None))
        self.groupBox1.setTitle(QCoreApplication.translate("Prepare_ArcaeaOfflineOcr", u"\u7ed3\u679c", None))
        self.executeButton.setText(QCoreApplication.translate("Prepare_ArcaeaOfflineOcr", u"\u6267\u884c", None))
        pass
    # retranslateUi

