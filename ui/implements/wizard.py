from PySide6.QtWidgets import QWizard
from ui.implements.pages import (
    Welcome,
    Prepare_ArcaeaOfflineOcr,
    Prepare_Tesseract,
    Crop_SelectScreenshot,
    Crop_Pure,
)

from PySide6.QtGui import QPixmap


class Wizard(QWizard):
    def __init__(self):
        super().__init__()
        self.setWizardStyle(QWizard.WizardStyle.ModernStyle)

        self.setPixmap(
            QWizard.WizardPixmap.WatermarkPixmap,
            QPixmap(":/images/watermark.png"),
        )

        crop_selectScreenshot = Crop_SelectScreenshot(self)
        crop_pure = Crop_Pure(self)

        crop_selectScreenshot.screenshotChanged.connect(crop_pure.setScreenshot)

        self.addPage(Welcome(self))
        self.addPage(Prepare_ArcaeaOfflineOcr(self))
        self.addPage(Prepare_Tesseract(self))
        self.addPage(crop_selectScreenshot)
        self.addPage(crop_pure)
