from arcaea_offline_ocr.recognize import recognize_score
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPixmap

from ..fields import SCORE_RECT
from .crop_general import Crop_General

translate = QCoreApplication.translate


class Crop_Score(Crop_General):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle("SCORE")

        self.registerField(SCORE_RECT, self, "selectionRect")

        self.descLabel.setText(translate("Crop", "请框选出得分区域：上下对齐"))
        self.setExampleImgLabelPixmap(QPixmap(":/arcaea-offline-ocr-device-creation-wizard/images/crop_score_example.jpg"))
        self.setRecognizeFunction(recognize_score)
