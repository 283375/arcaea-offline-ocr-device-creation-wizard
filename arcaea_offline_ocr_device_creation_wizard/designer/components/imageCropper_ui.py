# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imageCropper.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QWidget)

class Ui_ImageCropper(object):
    def setupUi(self, ImageCropper):
        if not ImageCropper.objectName():
            ImageCropper.setObjectName(u"ImageCropper")
        ImageCropper.resize(654, 273)
        ImageCropper.setWindowTitle(u"ImageCropper")
        self.horizontalLayout = QHBoxLayout(ImageCropper)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graphicsView = QGraphicsView(ImageCropper)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(400, 255))
        self.graphicsView.setMaximumSize(QSize(400, 225))

        self.horizontalLayout.addWidget(self.graphicsView)

        self.groupBox = QGroupBox(ImageCropper)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.topLeftPointTopSpinBox = QSpinBox(self.groupBox)
        self.topLeftPointTopSpinBox.setObjectName(u"topLeftPointTopSpinBox")

        self.gridLayout.addWidget(self.topLeftPointTopSpinBox, 1, 2, 1, 1)

        self.resizeTo100Button = QPushButton(self.groupBox)
        self.resizeTo100Button.setObjectName(u"resizeTo100Button")

        self.gridLayout.addWidget(self.resizeTo100Button, 6, 2, 1, 1)

        self.fitInViewButton = QPushButton(self.groupBox)
        self.fitInViewButton.setObjectName(u"fitInViewButton")

        self.gridLayout.addWidget(self.fitInViewButton, 6, 1, 1, 1)

        self.zoomInButton = QPushButton(self.groupBox)
        self.zoomInButton.setObjectName(u"zoomInButton")

        self.gridLayout.addWidget(self.zoomInButton, 5, 1, 1, 1)

        self.topLeftPointLeftSpinBox = QSpinBox(self.groupBox)
        self.topLeftPointLeftSpinBox.setObjectName(u"topLeftPointLeftSpinBox")

        self.gridLayout.addWidget(self.topLeftPointLeftSpinBox, 1, 1, 1, 1)

        self.zoomOutButton = QPushButton(self.groupBox)
        self.zoomOutButton.setObjectName(u"zoomOutButton")

        self.gridLayout.addWidget(self.zoomOutButton, 5, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.widthSpinBox = QSpinBox(self.groupBox)
        self.widthSpinBox.setObjectName(u"widthSpinBox")

        self.gridLayout.addWidget(self.widthSpinBox, 3, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.heightSpinBox = QSpinBox(self.groupBox)
        self.heightSpinBox.setObjectName(u"heightSpinBox")

        self.gridLayout.addWidget(self.heightSpinBox, 4, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)


        self.retranslateUi(ImageCropper)

        QMetaObject.connectSlotsByName(ImageCropper)
    # setupUi

    def retranslateUi(self, ImageCropper):
        self.groupBox.setTitle(QCoreApplication.translate("ImageCropper", u"\u5fae\u64cd", None))
        self.label_2.setText(QCoreApplication.translate("ImageCropper", u"\u5bbd", None))
        self.resizeTo100Button.setText(QCoreApplication.translate("ImageCropper", u"1:1", None))
        self.fitInViewButton.setText(QCoreApplication.translate("ImageCropper", u"\u9002\u5e94\u753b\u6846", None))
        self.zoomInButton.setText(QCoreApplication.translate("ImageCropper", u"\u653e\u5927", None))
        self.zoomOutButton.setText(QCoreApplication.translate("ImageCropper", u"\u7f29\u5c0f", None))
        self.label_3.setText(QCoreApplication.translate("ImageCropper", u"\u9ad8", None))
        self.label.setText(QCoreApplication.translate("ImageCropper", u"\u5de6\u4e0a\u89d2\u70b9", None))
        self.label_4.setText(QCoreApplication.translate("ImageCropper", u"\u5de6", None))
        self.label_5.setText(QCoreApplication.translate("ImageCropper", u"\u4e0a", None))
        pass
    # retranslateUi

