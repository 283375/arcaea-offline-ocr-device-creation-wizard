from arcaea_offline_ocr.recognize import recognize_rating_class
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPixmap
from ui.implements.fields import RATING_CLASS_RECT

from .crop_general import Crop_General

translate = QCoreApplication.translate


class Crop_RatingClass(Crop_General):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle("Rating Class")

        self.registerField(RATING_CLASS_RECT, self, "selectionRect")

        self.descLabel.setText(translate("Crop", "请框选出难度(PST/PRS/FTR/BYD)区域：适当留白"))
        self.setExampleImgLabelPixmap(QPixmap(":/images/crop_rating_class_example.jpg"))
        self.setRecognizeFunction(recognize_rating_class)
