from PySide6.QtCore import Property, QCoreApplication, Qt, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QGraphicsPixmapItem, QGraphicsScene, QWizardPage
from ui.designer.pages.crop_selectScreenshot_ui import Ui_Crop_SelectScreenshot
from ui.implements.fields import SCREENSHOT_PATH

translate = QCoreApplication.translate


class Crop_SelectScreenshot(Ui_Crop_SelectScreenshot, QWizardPage):
    screenshotPathChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setTitle(translate("Title", "框选"))
        self.setSubTitle(translate("Subtitle", "选择截图"))

        self.__screenshotPath = ""
        self.graphicsScene = QGraphicsScene(self)
        self.pixmapItem: QGraphicsPixmapItem | None = None
        self.registerField(SCREENSHOT_PATH, self, "screenshotPath")

        self.fileSelector.fileDialog.accepted.connect(self.setImage)

    def getScreenshotPath(self):
        return self.__screenshotPath

    def setScreenshotPath(self, path: str):
        self.__screenshotPath = path
        self.screenshotPathChanged.emit()

    screenshotPath = Property(
        str, getScreenshotPath, setScreenshotPath, screenshotPathChanged
    )

    def setImage(self):
        file = self.fileSelector.fileDialog.selectedFiles()[0]
        if file == self.screenshotPath:
            return

        if self.pixmapItem:
            self.graphicsScene.removeItem(self.pixmapItem)
        self.pixmapItem = QGraphicsPixmapItem(QPixmap(file))
        self.graphicsView.fitInView(self.pixmapItem, Qt.AspectRatioMode.KeepAspectRatio)
        self.graphicsScene.addItem(self.pixmapItem)
        self.graphicsView.setScene(self.graphicsScene)
        self.setField(SCREENSHOT_PATH, file)
        self.completeChanged.emit()

    def isComplete(self):
        return bool(self.field(SCREENSHOT_PATH))
