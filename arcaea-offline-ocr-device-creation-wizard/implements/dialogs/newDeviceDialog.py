from uuid import uuid4

from ui.designer.dialogs.newDeviceDialog_ui import Ui_NewDeviceDialog
from PySide6.QtWidgets import QDialog


class NewDeviceDialog(Ui_NewDeviceDialog, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.uuidLabel.setText(str(uuid4()))

    def data(self) -> tuple[str, str]:
        return (self.deviceNameEdit.text(), self.uuidLabel.text())
