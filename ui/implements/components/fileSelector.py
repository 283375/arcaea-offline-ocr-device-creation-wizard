from ui.designer.components.fileSelector_ui import Ui_FileSelector
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Property, Slot, Qt


class FileSelector(Ui_FileSelector, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fileDialog = QFileDialog(self)
        self.fileDialog.setObjectName("fileDialog")
        self.setupUi(self)
        self.elidedLabel.setElideMode(Qt.TextElideMode.ElideMiddle)

    @Slot()
    def on_pushButton_clicked(self):
        self.fileDialog.open()

    @Slot()
    def on_fileDialog_accepted(self):
        self.elidedLabel.setText("<br>".join(self.fileDialog.selectedFiles()))
