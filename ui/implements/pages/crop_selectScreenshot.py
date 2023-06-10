from ui.designer.pages.crop_selectScreenshot_ui import Ui_Crop_SelectScreenshot
from PySide6.QtWidgets import QWizardPage, QGraphicsScene
from PySide6.QtCore import QCoreApplication, Signal, Slot, Qt, Property
from PySide6.QtGui import QImage, QPixmap

from ui.implements.fields import SCREENSHOT_IMAGE

translate = QCoreApplication.translate


class Crop_SelectScreenshot(Ui_Crop_SelectScreenshot, QWizardPage):
    screenshotChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setTitle(translate("Title", "框选"))
        self.setSubTitle(translate("Subtitle", "选择截图"))

        self.graphicsScene = QGraphicsScene(self)
        self.__screenshot = None
        self.registerField(SCREENSHOT_IMAGE, self, "screenshot")

        self.fileSelector.fileDialog.accepted.connect(self.setImage)

    @Property(QImage, notify=screenshotChanged)
    def screenshot(self):
        return self.__screenshot

    @screenshot.setter
    def screenshot(self, value: QImage):
        self.__screenshot = value
        self.screenshotChanged.emit()

    def setImage(self):
        file = self.fileSelector.fileDialog.selectedFiles()[0]
        self.screenshot = QImage(file)
        self.graphicsScene.addPixmap(
            QPixmap.fromImage(self.__screenshot).scaled(180, 90)
        )
        self.graphicsView.setScene(self.graphicsScene)
        self.setField(SCREENSHOT_IMAGE, self.__screenshot)
        self.completeChanged.emit()

    def isComplete(self):
        return isinstance(self.__screenshot, QImage)
