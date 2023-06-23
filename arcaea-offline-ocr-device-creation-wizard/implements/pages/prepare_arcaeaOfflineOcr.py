from importlib.metadata import version

from PySide6.QtCore import QCoreApplication, Slot
from PySide6.QtWidgets import QWizardPage
from ui.designer.pages.prepare_arcaeaOfflineOcr_ui import Ui_Prepare_ArcaeaOfflineOcr

translate = QCoreApplication.translate


class Prepare_ArcaeaOfflineOcr(Ui_Prepare_ArcaeaOfflineOcr, QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setTitle(translate("Title", "准备工作"))
        self.setSubTitle(translate("SubTitle", "arcaea-offline-ocr"))

        self.checkVersion()

    @Slot()
    def on_executeButton_clicked(self):
        self.checkVersion()

    def checkVersion(self):
        ver = version("arcaea-offline-ocr")
        self.resultLabel.setText(str(ver) if ver is not None else "")
        self.completeChanged.emit()

    def validatePage(self):
        return bool(self.resultLabel.text())

    def isComplete(self):
        return bool(self.resultLabel.text())
