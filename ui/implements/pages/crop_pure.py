from ui.designer.pages.crop_general_ui import Ui_Crop_General
from PySide6.QtWidgets import QWizardPage, QGraphicsScene
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import QRect

from ui.implements.fields import SCREENSHOT_IMAGE


class Crop_Pure(Ui_Crop_General, QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setScreenshot()

    def setScreenshot(self):
        screenshotQImage = self.field(SCREENSHOT_IMAGE)  # type: QImage
        if screenshotQImage is not None:
            self.imageCropper.setPixmap(QPixmap.fromImage(screenshotQImage))
