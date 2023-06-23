# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'final_confirm.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_Final_Confirm(object):
    def setupUi(self, Final_Confirm):
        if not Final_Confirm.objectName():
            Final_Confirm.setObjectName(u"Final_Confirm")
        Final_Confirm.resize(633, 460)
        Final_Confirm.setWindowTitle(u"Final_Confirm")
        self.verticalLayout_2 = QVBoxLayout(Final_Confirm)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(Final_Confirm)
        self.widget.setObjectName(u"widget")
        self.formLayout = QFormLayout(self.widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.devicesJsonPathLabel = QLabel(self.widget)
        self.devicesJsonPathLabel.setObjectName(u"devicesJsonPathLabel")
        self.devicesJsonPathLabel.setText(u"...")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.devicesJsonPathLabel)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.deviceInfoLabel = QLabel(self.widget)
        self.deviceInfoLabel.setObjectName(u"deviceInfoLabel")
        self.deviceInfoLabel.setText(u"...")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.deviceInfoLabel)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_3)

        self.confirmButton = QPushButton(self.widget)
        self.confirmButton.setObjectName(u"confirmButton")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.confirmButton)


        self.verticalLayout_2.addWidget(self.widget)

        self.tableView = QTableView(Final_Confirm)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_2.addWidget(self.tableView)

        self.verticalLayout_2.setStretch(1, 1)

        self.retranslateUi(Final_Confirm)

        QMetaObject.connectSlotsByName(Final_Confirm)
    # setupUi

    def retranslateUi(self, Final_Confirm):
        self.label.setText(QCoreApplication.translate("Final_Confirm", u"\u5c06\u5411", None))
        self.label_2.setText(QCoreApplication.translate("Final_Confirm", u"\u4e2d\u7684", None))
        self.label_3.setText(QCoreApplication.translate("Final_Confirm", u"\u5199\u5165\u672c\u6b21\u914d\u7f6e\u7ed3\u679c\uff1a", None))
        self.confirmButton.setText(QCoreApplication.translate("Final_Confirm", u"\u786e\u8ba4\u5199\u5165", None))
        pass
    # retranslateUi

