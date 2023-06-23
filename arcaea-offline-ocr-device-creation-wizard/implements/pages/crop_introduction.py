from PySide6.QtWidgets import QWizardPage
from ui.designer.pages.crop_introduction_ui import Ui_Crop_Introduction


class Crop_Introduction(Ui_Crop_Introduction, QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
