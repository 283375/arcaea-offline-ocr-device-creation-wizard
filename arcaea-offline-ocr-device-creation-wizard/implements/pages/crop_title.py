from arcaea_offline_ocr.recognize import recognize_title
from PySide6.QtCore import QCoreApplication

from ui.implements.fields import TITLE_RECT

from .crop_general import Crop_General

translate = QCoreApplication.translate


class Crop_Title(Crop_General):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSubTitle("Title")

        self.registerField(TITLE_RECT, self, "selectionRect")

        self.descLabel.setText(translate("Crop", "请框选出标题区域：适当留白"))
        self.setRecognizeFunction(recognize_title)
