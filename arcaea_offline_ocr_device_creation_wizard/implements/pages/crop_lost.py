from arcaea_offline_ocr.recognize import recognize_far_lost
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPixmap

from ..fields import LOST_RECT
from .crop_general import Crop_General

translate = QCoreApplication.translate


class Crop_Lost(Crop_General):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle("LOST")

        self.registerField(LOST_RECT, self, "selectionRect")

        self.descLabel.setText(translate("Crop", "请框选出 LOST 区域：上下对齐"))
        self.setExampleImgLabelPixmap(QPixmap(":/arcaea-offline-ocr-device-creation-wizard/images/crop_lost_example.jpg"))
        self.setRecognizeFunction(recognize_far_lost)
