from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWizard, QWizardPage

from ...designer.pages.welcome_ui import Ui_Welcome

translate = QCoreApplication.translate


class Welcome(Ui_Welcome, QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setTitle(translate("Page_Welcome", "欢迎"))
