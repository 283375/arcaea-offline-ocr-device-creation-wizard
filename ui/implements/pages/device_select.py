from arcaea_offline_ocr.device import Device
from PySide6.QtCore import Property, QCoreApplication, QDir, QFile, QIODevice, Qt, Slot
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QMessageBox, QWizardPage

from ui.designer.pages.device_select_ui import Ui_Device_Select
from ui.extends.devices import load_devices_json
from ui.implements.dialogs.newDeviceDialog import NewDeviceDialog
from ui.implements.fields import DEVICE_NAME, DEVICE_UUID, DEVICES_JSON_PATH

translate = QCoreApplication.translate


class DevicesModel(QStandardItemModel):
    UuidRole = Qt.ItemDataRole.UserRole + 1
    NameRole = Qt.ItemDataRole.UserRole + 2

    def setDevices(self, devices: list[Device]):
        self.clear()

        for device in devices:
            item = QStandardItem(f"{device.name} | {device.uuid}")
            item.setData(device.uuid, self.UuidRole)
            item.setData(device.name, self.NameRole)
            self.appendRow(item)


class Device_Select(Ui_Device_Select, QWizardPage):
    def getDevicesJsonPath(self):
        return self.__devicesJsonPath

    def setDevicesJsonPath(self, path: str):
        self.__devicesJsonPath = path

    def getDeviceUuid(self):
        return self.__deviceUuid

    def setDeviceUuid(self, uuid: str):
        self.__deviceUuid = uuid

    def getDeviceName(self):
        return self.__deviceName

    def setDeviceName(self, name: str):
        self.__deviceName = name

    devicesJsonPath = Property(str, getDevicesJsonPath, setDevicesJsonPath)
    deviceUuid = Property(str, getDeviceUuid, setDeviceUuid)
    deviceName = Property(str, getDeviceName, setDeviceName)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setTitle(translate("Title", "device.select"))
        self.setSubTitle(translate("Subtitle", "device.select"))

        self.__devicesJsonPath = None
        self.__deviceUuid = ""
        self.__deviceName = ""
        self.registerField(DEVICES_JSON_PATH, self, "devicesJsonPath")
        self.registerField(DEVICE_UUID, self, "deviceUuid")
        self.registerField(DEVICE_NAME, self, "deviceName")

        self.__devicesModel = DevicesModel(self)
        self.existingDevicesComboBox.setModel(self.__devicesModel)

        self.fileSelector.fileDialog.accepted.connect(
            lambda: self.setDevicesJson(
                QFile(self.fileSelector.fileDialog.selectedFiles()[0])
            )
        )

    def setDeviceOptions(self, uuid: str, name: str):
        self.setField(DEVICE_UUID, uuid)
        self.setField(DEVICE_NAME, name)
        self.completeChanged.emit()

    @Slot()
    def on_currentDirButton_clicked(self):
        result = QMessageBox.warning(
            self,
            "Warning",
            translate("Page_Device", "device.currentDirWarning"),
            QMessageBox.StandardButton.Yes,
            QMessageBox.StandardButton.No,
        )
        if result == QMessageBox.StandardButton.Yes:
            file = QFile(QDir.current().absoluteFilePath("devices.json"))
            if not file.exists():
                file.open(QIODevice.OpenModeFlag.WriteOnly)
                file.close()
            self.setDevicesJson(file)

    @Slot()
    def on_newDeviceButton_clicked(self):
        self.__newDeviceDialog = NewDeviceDialog(self)
        self.__newDeviceDialog.accepted.connect(self.newDeviceDialogAccepted)
        self.__newDeviceDialog.open()

    @Slot()
    def on_existingDevicesComboBox_activated(self):
        if self.existingDevicesComboBox.currentIndex() > -1:
            self.setDeviceOptions(
                self.existingDevicesComboBox.currentData(DevicesModel.UuidRole),
                self.existingDevicesComboBox.currentData(DevicesModel.NameRole),
            )

    def newDeviceDialogAccepted(self):
        name, uuid = self.__newDeviceDialog.data()
        self.setDeviceOptions(uuid, name)
        self.__newDeviceDialog.deleteLater()

    def setDevicesJson(self, file: QFile):
        try:
            devices = load_devices_json(file.fileName())
            self.actionsWidget.setEnabled(True)
            self.__devicesModel.setDevices(devices)
            self.existingDevicesComboBox.setCurrentIndex(-1)
            self.setField(DEVICES_JSON_PATH, file.fileName())
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            self.actionsWidget.setEnabled(False)

    def isComplete(self):
        return bool(
            self.field(DEVICES_JSON_PATH)
            and self.field(DEVICE_UUID)
            and self.field(DEVICE_NAME)
        )

    def validatePage(self):
        devicesJsonPath: str = self.field(DEVICES_JSON_PATH)
        uuid: str = self.field(DEVICE_UUID)
        name: str = self.field(DEVICE_NAME)

        if QFile(devicesJsonPath).exists() and uuid and name:
            result = QMessageBox.information(
                self,
                "Confirm",
                translate("Page_Device", "device.confirmInput"),
                QMessageBox.StandardButton.Yes,
                QMessageBox.StandardButton.No,
            )
            return result == QMessageBox.StandardButton.Yes
        else:
            QMessageBox.critical(
                self, "Error", translate("Page_Device", "device.incompleteInput")
            )
            return False