from PySide6.QtWidgets import QWizard
from ui.implements.pages import (
    Welcome,
    Prepare_ArcaeaOfflineOcr,
    Prepare_Tesseract,
    Device_Select,
    Crop_Introduction,
    Crop_SelectScreenshot,
    Crop_Pure,
    Crop_Far,
    Crop_Lost,
    Crop_Score,
    Crop_MaxRecall,
    Crop_RatingClass,
    Crop_Title,
    Final_Confirm,
)
from ui.extends.devices import qRect_to_device_rect
from arcaea_offline_ocr.device import Device
from .fields import (
    DEVICE_UUID,
    DEVICE_NAME,
    PURE_RECT,
    FAR_RECT,
    LOST_RECT,
    SCORE_RECT,
    MAX_RECALL_RECT,
    RATING_CLASS_RECT,
    TITLE_RECT,
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QRect


class Wizard(QWizard):
    def __init__(self):
        super().__init__()
        self.setWizardStyle(QWizard.WizardStyle.ModernStyle)

        self.setPixmap(
            QWizard.WizardPixmap.WatermarkPixmap,
            QPixmap(":/images/watermark.png"),
        )

        crop_selectScreenshot = Crop_SelectScreenshot(self)
        crop_pure = Crop_Pure(self)
        crop_far = Crop_Far(self)
        crop_lost = Crop_Lost(self)
        crop_score = Crop_Score(self)
        crop_max_recall = Crop_MaxRecall(self)
        crop_rating_class = Crop_RatingClass(self)
        crop_title = Crop_Title(self)

        self.currentIdChanged.connect(self.autoSetSelectionRect)

        self.addPage(Welcome(self))
        self.addPage(Prepare_ArcaeaOfflineOcr(self))
        self.addPage(Prepare_Tesseract(self))
        self.addPage(Device_Select(self))
        self.addPage(Crop_Introduction(self))
        self.addPage(crop_selectScreenshot)
        self.crop_pure_pageId = self.addPage(crop_pure)
        self.crop_far_pageId = self.addPage(crop_far)
        self.crop_lost_pageId = self.addPage(crop_lost)
        self.addPage(crop_score)
        self.crop_max_recall_pageId = self.addPage(crop_max_recall)
        self.crop_rating_class_pageId = self.addPage(crop_rating_class)
        self.addPage(crop_title)
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
