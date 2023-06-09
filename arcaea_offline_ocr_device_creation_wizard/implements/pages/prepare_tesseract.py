import pytesseract
from cv2 import COLOR_RGBA2BGR, cvtColor
from PySide6.QtCore import QCoreApplication, Signal, Slot
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QMessageBox, QWizardPage

from ...designer.pages.prepare_tesseract_ui import Ui_Prepare_Tesseract
from ...extends.utils import qImage2cvMatRGBA
from ..fields import TESSDATA_PATH, TESSERACT_PATH

translate = QCoreApplication.translate


class Prepare_Tesseract(Ui_Prepare_Tesseract, QWizardPage):
    tesseractPathChanged = Signal()
    tessdataPathChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setTitle(translate("Title", "准备工作"))
        self.setSubTitle(translate("SubTitle", "tesseract"))

        self.image = QImage(":/arcaea-offline-ocr-device-creation-wizard/images/ocr_test.png")
        self.pixmap = QPixmap.fromImage(self.image)

        self.__tesseractPath = ""
        self.__tessdataPath = ""
        self.registerField(
            TESSERACT_PATH, self, "__tesseractPath", "tesseractPathChanged"
        )
        self.registerField(TESSDATA_PATH, self, "__tessdataPath", "tessdataPathChanged")

        self.imageLabel.setPixmap(self.pixmap)

        self.tesseractFileSelector.fileDialog.accepted.connect(self.setTesseractPath)
        self.tessdataFileSelector.fileDialog.accepted.connect(self.setTessdataPath)

    def setTesseractPath(self):
        self.__tesseractPath = self.tesseractFileSelector.fileDialog.selectedFiles()[0]
        self.tesseractPathChanged.emit()

    def setTessdataPath(self):
        self.__tessdataPath = self.tessdataFileSelector.fileDialog.selectedFiles()[0]
        self.tessdataPathChanged.emit()

    @Slot()
    def on_executeButton_clicked(self):
        pytesseract.pytesseract.tesseract_cmd = self.__tesseractPath
        cv2Mat = qImage2cvMatRGBA(self.image)
        cv2Mat = cvtColor(cv2Mat, COLOR_RGBA2BGR)
        result = pytesseract.image_to_string(cv2Mat).replace("\n", "")
        self.resultLabel.setText(result)
        self.completeChanged.emit()

    def validatePage(self):
        resultText = self.resultLabel.text()
        if resultText == "Trig 283375":
            return True

        button = QMessageBox.warning(
            self,
            None,
            translate("DetectTesseract", "文字可能与图片不匹配。确定继续吗？"),
            QMessageBox.StandardButton.Ok,
            QMessageBox.StandardButton.Cancel,
        )

        return button == QMessageBox.StandardButton.Ok

    def isComplete(self):
        return True
