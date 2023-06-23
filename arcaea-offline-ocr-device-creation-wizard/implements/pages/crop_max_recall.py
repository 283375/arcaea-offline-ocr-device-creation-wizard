from arcaea_offline_ocr.recognize import recognize_max_recall
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPixmap

from ui.implements.fields import MAX_RECALL_RECT

from .crop_general import Crop_General

translate = QCoreApplication.translate


class Crop_MaxRecall(Crop_General):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle("MAX RECALL")

        self.registerField(MAX_RECALL_RECT, self, "selectionRect")

        self.descLabel.setText(translate("Crop", "请框选出最高连击区域：适当留白"))
        self.setExampleImgLabelPixmap(QPixmap(":/images/crop_max_recall_example.jpg"))
        self.setRecognizeFunction(recognize_max_recall)
