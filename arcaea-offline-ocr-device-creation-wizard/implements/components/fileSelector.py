from PySide6.QtCore import QFile, Qt, Signal, Slot
from PySide6.QtWidgets import QFileDialog, QWidget

from ...designer.components.fileSelector_ui import Ui_FileSelector


class FileSelector(Ui_FileSelector, QWidget):
    accepted = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.fileDialog = QFileDialog(self)
        self.fileDialog.setObjectName("fileDialog")
        self.setupUi(self)
        self.elidedLabel.setElideMode(Qt.TextElideMode.ElideMiddle)

        self.fileDialog.accepted.connect(self.accepted)
        self.selectedFiles = self.fileDialog.selectedFiles
        self.setNameFilters = self.fileDialog.setNameFilters

    @Slot()
    def on_pushButton_clicked(self):
        self.fileDialog.open()

    @Slot()
    def on_fileDialog_filesSelected(self):
        self.__updateLabel(self.fileDialog.selectedFiles())

    def __updateLabel(self, list_str: list[str]):
        self.elidedLabel.setText("<br>".join(list_str))

    def selectFile(self, filename: str):
        if QFile(filename).exists():
            self.fileDialog.selectFile(filename)
            self.__updateLabel([filename])
