from PySide6.QtCore import Property, QCoreApplication, QRect, Signal
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QMessageBox, QWizardPage

from ui.designer.pages.crop_general_ui import Ui_Crop_General
from ui.implements.fields import SCREENSHOT_IMAGE

translate = QCoreApplication.translate


class Crop_General(Ui_Crop_General, QWizardPage):
    selectionRectChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setTitle(translate("Title", "裁剪"))

        self.setScreenshot()

        self.imageCropper.selectionRectChanged.connect(self.selectionRectChanged)
        self.imageCropper.selectionRectChanged.connect(self.completeChanged)

    def setScreenshot(self):
        screenshotQImage = self.field(SCREENSHOT_IMAGE)  # type: QImage
        if screenshotQImage is not None:
            self.imageCropper.setPixmap(QPixmap.fromImage(screenshotQImage))

    def getSelectionRect(self):
        return self.imageCropper.selectionRect()

    def setSelectionRect(self, rect: QRect):
        self.imageCropper.setSelectionRect(rect)

    selectionRect = Property(
        QRect, getSelectionRect, setSelectionRect, notify=selectionRectChanged
    )

    def isComplete(self):
        return self.selectionRect.isValid()

    def validatePage(self):
        if not self.resultLabel.text():
            result = QMessageBox.warning(
                self,
                None,
                translate("Crop", "可能还未尝试识别，是否继续？"),
                QMessageBox.StandardButton.Ok,
                QMessageBox.StandardButton.Cancel,
            )
            return result == QMessageBox.StandardButton.Ok

        return self.isComplete()
