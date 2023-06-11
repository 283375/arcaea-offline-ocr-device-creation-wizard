# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'device_select.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from ui.implements.components.fileSelector import FileSelector

class Ui_Device_Select(object):
    def setupUi(self, Device_Select):
        if not Device_Select.objectName():
            Device_Select.setObjectName(u"Device_Select")
        Device_Select.resize(500, 400)
        Device_Select.setWindowTitle(u"DeviceSelect")
        self.verticalLayout = QVBoxLayout(Device_Select)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(Device_Select)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label)

        self.currentDirButton = QPushButton(Device_Select)
        self.currentDirButton.setObjectName(u"currentDirButton")

        self.horizontalLayout.addWidget(self.currentDirButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.fileSelector = FileSelector(Device_Select)
        self.fileSelector.setObjectName(u"fileSelector")

        self.verticalLayout.addWidget(self.fileSelector)

        self.actionsWidget = QWidget(Device_Select)
        self.actionsWidget.setObjectName(u"actionsWidget")
        self.actionsWidget.setEnabled(False)
        self.formLayout = QFormLayout(self.actionsWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.actionsWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.newDeviceButton = QPushButton(self.actionsWidget)
        self.newDeviceButton.setObjectName(u"newDeviceButton")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.newDeviceButton)

        self.label_3 = QLabel(self.actionsWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.existingDevicesComboBox = QComboBox(self.actionsWidget)
        self.existingDevicesComboBox.setObjectName(u"existingDevicesComboBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.existingDevicesComboBox)


        self.verticalLayout.addWidget(self.actionsWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Device_Select)

        QMetaObject.connectSlotsByName(Device_Select)
    # setupUi

    def retranslateUi(self, Device_Select):
        self.label.setText(QCoreApplication.translate("Device_Select", u"\u8bf7\u9009\u62e9\u4e00\u4e2a\u8bbe\u5907\u5b9a\u4e49\u6587\u4ef6\uff08devices.json\uff09", None))
        self.currentDirButton.setText(QCoreApplication.translate("Device_Select", u"\u5f53\u524d\u76ee\u5f55", None))
        self.label_2.setText(QCoreApplication.translate("Device_Select", u"\u521b\u5efa\u65b0\u8bbe\u5907", None))
        self.newDeviceButton.setText(QCoreApplication.translate("Device_Select", u"\u914d\u7f6e\u2026", None))
        self.label_3.setText(QCoreApplication.translate("Device_Select", u"\u7f16\u8f91\u73b0\u6709\u8bbe\u5907", None))
        pass
    # retranslateUi

