from arcaea_offline_ocr.recognize import recognize_pure
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPixmap
from ui.implements.fields import PURE_RECT

from .crop_general import Crop_General

translate = QCoreApplication.translate


class Crop_Pure(Crop_General):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle("PURE")

        self.registerField(PURE_RECT, self, "selectionRect")

        self.descLabel.setText(translate("Crop", "请框选出 PURE 区域：上下对齐"))
        self.setExampleImgLabelPixmap(QPixmap(":/images/crop_pure_example.jpg"))
        self.setRecognizeFunction(recognize_pure)
