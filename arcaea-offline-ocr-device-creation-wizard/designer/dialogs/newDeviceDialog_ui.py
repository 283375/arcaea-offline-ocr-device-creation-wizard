# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newDeviceDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_NewDeviceDialog(object):
    def setupUi(self, NewDeviceDialog):
        if not NewDeviceDialog.objectName():
            NewDeviceDialog.setObjectName(u"NewDeviceDialog")
        NewDeviceDialog.resize(300, 100)
        NewDeviceDialog.setMinimumSize(QSize(300, 100))
        self.verticalLayout = QVBoxLayout(NewDeviceDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(NewDeviceDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.uuidLabel = QLabel(NewDeviceDialog)
        self.uuidLabel.setObjectName(u"uuidLabel")
        self.uuidLabel.setText(u"...")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.uuidLabel)

        self.label = QLabel(NewDeviceDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.deviceNameEdit = QLineEdit(NewDeviceDialog)
        self.deviceNameEdit.setObjectName(u"deviceNameEdit")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.deviceNameEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.buttonBox = QDialogButtonBox(NewDeviceDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(NewDeviceDialog)
        self.buttonBox.accepted.connect(NewDeviceDialog.accept)
        self.buttonBox.rejected.connect(NewDeviceDialog.reject)

        QMetaObject.connectSlotsByName(NewDeviceDialog)
    # setupUi

    def retranslateUi(self, NewDeviceDialog):
        NewDeviceDialog.setWindowTitle(QCoreApplication.translate("NewDeviceDialog", u"\u65b0\u5efa\u8bbe\u5907", None))
        self.label_2.setText(QCoreApplication.translate("NewDeviceDialog", u"UUID", None))
        self.label.setText(QCoreApplication.translate("NewDeviceDialog", u"\u8bbe\u5907\u5907\u6ce8", None))
    # retranslateUi

