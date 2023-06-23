import sys

from arcaea_offline_ocr_device_creation_wizard.implements.wizard import Wizard
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication()
    wizard = Wizard()
    wizard.show()
    sys.exit(app.exec())
