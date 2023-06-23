from arcaea_offline_ocr.recognize import recognize_far_lost
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPixmap

from ui.implements.fields import FAR_RECT

from .crop_general import Crop_General

translate = QCoreApplication.translate


class Crop_Far(Crop_General):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle("FAR")

        self.registerField(FAR_RECT, self, "selectionRect")

        self.descLabel.setText(translate("Crop", "请框选出 FAR 区域：上下对齐"))
        self.setExampleImgLabelPixmap(QPixmap(":/images/crop_far_example.jpg"))
        self.setRecognizeFunction(recognize_far_lost)
