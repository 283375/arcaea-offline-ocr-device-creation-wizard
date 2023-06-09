import sys
from PySide6.QtWidgets import QApplication

from ui.implements.wizard import Wizard
import ui.images.images_rc
import ui.translations.translations_rc

if __name__ == '__main__':
    app = QApplication()
    wizard = Wizard()
    wizard.setWindowTitle("arcaea-offline-ocr Device Creation Wizard")
    wizard.show()
    sys.exit(app.exec())
