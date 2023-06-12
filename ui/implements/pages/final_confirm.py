from arcaea_offline_ocr.device import Device
from arcaea_offline_ocr.recognize import recognize
from PySide6.QtCore import (
    QAbstractTableModel,
    QCoreApplication,
    QModelIndex,
    Qt,
    QRect,
    QSize,
)
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import QStyledItemDelegate, QWizard, QWizardPage

from ui.designer.pages.final_confirm_ui import Ui_Final_Confirm
from ui.implements.fields import (
    FAR_RECT,
    LOST_RECT,
    MAX_RECALL_RECT,
    PURE_RECT,
    RATING_CLASS_RECT,
    SCORE_RECT,
    SCREENSHOT_PATH,
    TITLE_RECT,
)

translate = QCoreApplication.translate


class DeviceResultModel(QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setHorizontalHeaders()
        self.__items = [
            ["PURE", None, None],
            ["FAR", None, None],
            ["LOST", None, None],
            ["SCORE", None, None],
            ["MAX RECALL", None, None],
            ["RATING CLASS", None, None],
            ["TITLE", None, None],
        ]

    def setHorizontalHeaders(self):
        self.__horizontalHeaders = [
            "",
            translate("Final", "final.resultTable.header.selection"),
            translate("Final", "final.resultTable.header.result"),
        ]

    def retranslateUi(self):
        self.setHorizontalHeaders()

    def headerData(self, section: int, orientation: Qt.Orientation, role: int):
        if (
            orientation == Qt.Orientation.Horizontal
            and role == Qt.ItemDataRole.DisplayRole
            and 0 <= section < len(self.__horizontalHeaders)
        ):
            return self.__horizontalHeaders[section]
        return None

    def rowCount(self, *args):
        return len(self.__items)

    def columnCount(self, *args):
        return len(self.__horizontalHeaders)

    def data(self, index: QModelIndex, role: int):
        if 0 <= index.row() < len(self.__items):
            if index.column() in [0, 1, 2] and role == Qt.ItemDataRole.DisplayRole:
                return self.__items[index.row()][index.column()]
            # elif index.column() == 1 and role == Qt.ItemDataRole.UserRole + 1:
            #     return self.__items[index.row()][index.column()]
            else:
                return None
        return None

    def update(self, wizard: QWizard):
        if (
            hasattr(wizard, "device")
            and callable(wizard.device)
            and isinstance(wizard.device(), Device)
        ):
            result = recognize(wizard.field(SCREENSHOT_PATH), wizard.device())
            results = [
                result.pure,
                result.far,
                result.lost,
                result.score,
                result.max_recall,
                result.rating_class,
                result.title,
            ]
            rects = [
                wizard.field(PURE_RECT),
                wizard.field(FAR_RECT),
                wizard.field(LOST_RECT),
                wizard.field(SCORE_RECT),
                wizard.field(MAX_RECALL_RECT),
                wizard.field(RATING_CLASS_RECT),
                wizard.field(TITLE_RECT),
            ]
            pixmap = QPixmap(wizard.field(SCREENSHOT_PATH))
            pixmap_selections = [
                pixmap.copy(rect).scaled(
                    250,
                    250,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
                for rect in rects
            ]

            self.beginResetModel()
            self.beginRemoveRows(QModelIndex(), 0, self.rowCount() - 1)
            self.endRemoveRows()
            self.beginInsertRows(QModelIndex(), 0, self.rowCount() - 1)
            for i in range(len(self.__items)):
                self.__items[i][1] = pixmap_selections[i]
                self.__items[i][2] = results[i]
            self.endInsertRows()
            self.endResetModel()
            print(self.__items)


class SimplePixmapDelegate(QStyledItemDelegate):
    def paint(self, painter: QPainter, option, index: QModelIndex):
        pixmap = index.data(Qt.ItemDataRole.DisplayRole)
        if isinstance(pixmap, QPixmap):
            self.sizeHintChanged.emit()
            rect: QRect = option.rect
            painter.drawPixmap(rect.x(), rect.y(), pixmap)
        else:
            super().paint(painter, option, index)

    def sizeHint(self, option, index: QModelIndex):
        pixmap = index.data(Qt.ItemDataRole.DisplayRole)
        return pixmap.size() if isinstance(pixmap, QPixmap) else QSize(0, 0)


class Final_Confirm(Ui_Final_Confirm, QWizardPage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setTitle(translate("Title", "final"))
        self.setSubTitle(translate("Subtitle", "final.confirm"))

        self.__model = DeviceResultModel(self)
        self.tableView.setModel(self.__model)
        # self.tableView.setItemDelegateForColumn(1, SimplePixmapDelegate(self.__model))

    def initializePage(self):
        self.__model.update(self.wizard())
        return super().initializePage()