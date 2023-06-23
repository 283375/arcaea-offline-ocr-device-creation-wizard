from arcaea_offline_ocr.device import Device
from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QSizePolicy, QVBoxLayout, QWidget, QWizard

from ..extends.devices import (
    load_devices_json,
    qRect_to_device_rect,
    write_devices_json,
)
from .fields import (
    DEVICE_NAME,
    DEVICE_UUID,
    DEVICES_JSON_PATH,
    FAR_RECT,
    LOST_RECT,
    MAX_RECALL_RECT,
    PURE_RECT,
    RATING_CLASS_RECT,
    SCORE_RECT,
    TITLE_RECT,
)
from .pages import (
    Crop_Far,
    Crop_Introduction,
    Crop_Lost,
    Crop_MaxRecall,
    Crop_Pure,
    Crop_RatingClass,
    Crop_Score,
    Crop_SelectScreenshot,
    Crop_Title,
    Device_Select,
    Final_Confirm,
    Prepare_ArcaeaOfflineOcr,
    Prepare_Tesseract,
    Welcome,
)


class WatermarkPixmapWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vLayout = QVBoxLayout(self)
        self.vLayout.setContentsMargins(0, 0, 0, 0)
        self.pixmapLabel = QLabel(self)
        self.pixmapLabel.setSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum
        )
        self.vLayout.addWidget(self.pixmapLabel)

    def setPixmap(self, pixmap: QPixmap):
        self.pixmapLabel.setPixmap(pixmap)
        self.pixmapLabel.setMinimumSize(pixmap.size())


class Wizard(QWizard):
    def __init__(self):
        super().__init__()
        self.resize(900, 600)
        self.setWizardStyle(QWizard.WizardStyle.ModernStyle)
        self.setOptions(
            QWizard.WizardOption.NoBackButtonOnLastPage
            | QWizard.WizardOption.NoBackButtonOnStartPage
        )
        self.setWindowFlags(
            self.windowFlags()
            | Qt.WindowType.CustomizeWindowHint
            | Qt.WindowType.WindowMinimizeButtonHint
            | Qt.WindowType.Window
        )
        watermarkPixmapWidget = WatermarkPixmapWidget(self)
        watermarkPixmapWidget.setPixmap(QPixmap(":/images/watermark.png"))
        self.setSideWidget(watermarkPixmapWidget)
        self.setMinimumHeight(
            watermarkPixmapWidget.layout().minimumSize().height() + 200
        )

        self.currentIdChanged.connect(self.autoSetSelectionRect)

        self.addPage(Welcome(self))
        self.addPage(Prepare_ArcaeaOfflineOcr(self))
        self.addPage(Prepare_Tesseract(self))
        self.addPage(Device_Select(self))
        self.addPage(Crop_Introduction(self))
        self.addPage(Crop_SelectScreenshot(self))
        self.crop_pure_pageId = self.addPage(Crop_Pure(self))
        self.crop_far_pageId = self.addPage(Crop_Far(self))
        self.crop_lost_pageId = self.addPage(Crop_Lost(self))
        self.addPage(Crop_Score(self))
        self.crop_max_recall_pageId = self.addPage(Crop_MaxRecall(self))
        self.crop_rating_class_pageId = self.addPage(Crop_RatingClass(self))
        self.addPage(Crop_Title(self))
        self.addPage(Final_Confirm(self))

    def autoSetSelectionRect(self):
        crop_pure = self.page(self.crop_pure_pageId)  # type: Crop_Pure
        crop_far = self.page(self.crop_far_pageId)  # type: Crop_Far
        crop_lost = self.page(self.crop_lost_pageId)  # type: Crop_Lost
        crop_max_recall = self.page(self.crop_max_recall_pageId)  # type: Crop_MaxRecall
        crop_rating_class = self.page(
            self.crop_rating_class_pageId
        )  # type: Crop_RatingClass
        pureSelectionRect = crop_pure.selectionRect  # type: QRect
        farSelectionRect = crop_far.selectionRect  # type: QRect
        lostSelectionRect = crop_lost.selectionRect  # type: QRect
        maxRecallSelectionRect = crop_max_recall.selectionRect  # type: QRect
        ratingClassSelectionRect = crop_rating_class.selectionRect  # type: QRect

        if (
            self.currentId() == self.crop_lost_pageId
            and not lostSelectionRect.isValid()
            and farSelectionRect
            and pureSelectionRect
        ):
            lost_auto_rect = QRect(
                pureSelectionRect.left(),
                farSelectionRect.top()
                + (farSelectionRect.top() - pureSelectionRect.top()),
                farSelectionRect.width(),
                farSelectionRect.height(),
            )
            crop_lost.setSelectionRect(lost_auto_rect)

        if (
            self.currentId() == self.crop_far_pageId
            and not farSelectionRect.isValid()
            and pureSelectionRect
        ):
            move_down_offset = round(pureSelectionRect.height() * 1.25)
            crop_far.setSelectionRect(
                pureSelectionRect.adjusted(0, move_down_offset, 0, move_down_offset)
            )

        if (
            self.currentId() == self.crop_rating_class_pageId
            and not ratingClassSelectionRect.isValid()
        ):
            crop_rating_class.setSelectionRect(
                maxRecallSelectionRect.adjusted(
                    0,
                    maxRecallSelectionRect.height(),
                    0,
                    maxRecallSelectionRect.height(),
                )
            )

    def device(self):
        uuid = self.field(DEVICE_UUID)
        name = self.field(DEVICE_NAME)
        pureRect = self.field(PURE_RECT)
        farRect = self.field(FAR_RECT)
        lostRect = self.field(LOST_RECT)
        scoreRect = self.field(SCORE_RECT)
        maxRecallRect = self.field(MAX_RECALL_RECT)
        ratingClassRect = self.field(RATING_CLASS_RECT)
        titleRect = self.field(TITLE_RECT)

        if (
            uuid
            and name
            and pureRect
            and farRect
            and lostRect
            and scoreRect
            and maxRecallRect
            and ratingClassRect
            and titleRect
        ):
            return Device(
                version=1,
                uuid=uuid,
                name=name,
                pure=qRect_to_device_rect(pureRect),
                far=qRect_to_device_rect(farRect),
                lost=qRect_to_device_rect(lostRect),
                max_recall=qRect_to_device_rect(maxRecallRect),
                rating_class=qRect_to_device_rect(ratingClassRect),
                score=qRect_to_device_rect(scoreRect),
                title=qRect_to_device_rect(titleRect),
            )

        return None

    def writeDevice(self):
        devicesJsonPath = self.field(DEVICES_JSON_PATH)
        device = self.device()
        if devicesJsonPath and device is not None:
            devices = load_devices_json(devicesJsonPath)
            index = next(
                (
                    i
                    for i, deviceInFile in enumerate(devices)
                    if deviceInFile.uuid == device.uuid
                ),
                -1,
            )
            if index > -1:
                devices[index] = device
            else:
                devices.append(device)
            write_devices_json(devicesJsonPath, devices)
