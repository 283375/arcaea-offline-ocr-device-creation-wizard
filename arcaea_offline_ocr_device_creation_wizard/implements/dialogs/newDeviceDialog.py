from uuid import uuid4

from PySide6.QtWidgets import QDialog

from ...designer.dialogs.newDeviceDialog_ui import Ui_NewDeviceDialog


class NewDeviceDialog(Ui_NewDeviceDialog, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.uuidLabel.setText(str(uuid4()))

    def data(self) -> tuple[str, str]:
        return (self.deviceNameEdit.text(), self.uuidLabel.text())
