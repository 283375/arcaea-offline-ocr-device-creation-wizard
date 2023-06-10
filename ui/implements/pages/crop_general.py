from PySide6.QtCore import Property, QCoreApplication, QRect, Signal, Qt, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QMessageBox, QWizardPage

from ui.designer.pages.crop_general_ui import Ui_Crop_General
from ui.extends.utils import qImage2cvMatRGBA
from ui.implements.fields import SCREENSHOT_IMAGE

from cv2 import cvtColor, COLOR_RGBA2BGR, COLOR_BGR2HSV

translate = QCoreApplication.translate


class Crop_General(Ui_Crop_General, QWizardPage):
    selectionRectChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setTitle(translate("Title", "框选"))

        self.setScreenshot()

        self.imageCropper.selectionRectChanged.connect(self.selectionRectChanged)
        self.imageCropper.selectionRectChanged.connect(self.completeChanged)

    def setScreenshot(self):
        screenshotQImage = self.field(SCREENSHOT_IMAGE)  # type: QImage
        if screenshotQImage is not None:
            self.imageCropper.setPixmap(QPixmap.fromImage(screenshotQImage))

    def setExampleImgLabelPixmap(self, pixmap: QPixmap):
        scaled_pixmap = pixmap.scaled(
            self.exampleImgLabel.maximumWidth(),
            pixmap.height(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        self.exampleImgLabel.setPixmap(scaled_pixmap)

    @Slot()
    def on_executeButton_clicked(self):
        self.recognize()

    def setRecognizeFunction(self, func):
        self.__recognizeFunction = func

    def recognize(self):
        cv2Mat = qImage2cvMatRGBA(self.imageCropper.selectionPixmap().toImage())
        cv2Mat = cvtColor(cv2Mat, COLOR_RGBA2BGR)
        cv2Mat = cvtColor(cv2Mat, COLOR_BGR2HSV)
        result = self.__recognizeFunction(cv2Mat)
        self.resultLabel.setText(str(result))

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
