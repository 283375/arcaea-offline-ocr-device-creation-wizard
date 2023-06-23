from PySide6.QtCore import Property, QPoint, QRect, QRectF, Qt, Signal, Slot
from PySide6.QtGui import QColor, QPainterPath, QPen, QPixmap
from PySide6.QtWidgets import (
    QGraphicsPathItem,
    QGraphicsPixmapItem,
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsSceneMouseEvent,
    QWidget,
)

from ...designer.components.imageCropper_ui import Ui_ImageCropper
from ...extends.graphics import GraphicsViewZoomWrapper


class CropGraphicsScene(QGraphicsScene):
    selectionRectChanged = Signal()
    selectionRectChangedByDrag = Signal()
    selectionRectChangedBySet = Signal()
    viewSceneRectChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

        self.selectionRectChangedByDrag.connect(self.selectionRectChanged)
        self.selectionRectChangedBySet.connect(self.selectionRectChanged)

        self.__selectionRect = QRect()
        self.__origDragMaskPath = None
        self.__dragMask = QGraphicsPathItem()
        self.__dragMask.setPen(Qt.PenStyle.NoPen)
        self.__dragMask.setBrush(QColor(0, 0, 0, 128))
        self.__dragMask.hide()
        self.addItem(self.__dragMask)
        self.__selectionRectBorderItem = QGraphicsRectItem()
        self.__selectionRectBorderItemPen = QPen(QColor("#27a6e5"))
        self.__selectionRectBorderItemPen.setWidth(4)
        self.__selectionRectBorderItem.setPen(self.__selectionRectBorderItemPen)
        self.__selectionRectBorderItem.hide()
        self.addItem(self.__selectionRectBorderItem)
        self.__pixmapItem = None

        self.__dragging = False
        self.__startScenePos = QPoint()

    def selectionRect(self):
        return self.__selectionRect

    def setSelectionRect(self, value: QRect):
        self.__selectionRect = (
            self.__pixmapItem.boundingRect().toRect() & value.normalized()
        )
        self.drawSelectionRect(self.__selectionRect)
        self.selectionRectChangedBySet.emit()

    def selectionPixmap(self):
        return self.__pixmapItem.pixmap().copy(self.__selectionRect)

    @Property(QRectF)
    def viewSceneRect(self) -> QRectF:
        return self.sceneRect() & self.__pixmapItem.sceneBoundingRect()

    def setPixmap(self, pixmap: QPixmap):
        if self.__pixmapItem:
            if pixmap.cacheKey() == self.__pixmapItem.pixmap().cacheKey():
                return
            self.removeItem(self.__pixmapItem)
        self.__pixmapItem = QGraphicsPixmapItem(pixmap)
        self.addItem(self.__pixmapItem)
        self.__dragMask.setZValue(self.__pixmapItem.zValue() + 1)
        self.__selectionRectBorderItem.setZValue(self.__pixmapItem.zValue() + 2)

        dragMaskPath = QPainterPath()
        dragMaskPath.addRect(self.__pixmapItem.boundingRect())
        self.__origDragMaskPath = dragMaskPath

        self.viewSceneRectChanged.emit()

    def calculateSelectionRect(self, point: QPoint):
        width = abs(point.x() - self.__startScenePos.x())
        height = abs(point.y() - self.__startScenePos.y())
        left = min(point.x(), self.__startScenePos.x())
        top = min(point.y(), self.__startScenePos.y())
        return QRect(left, top, width, height)

    def drawSelectionRect(self, selectionRect: QRect):
        if not selectionRect.isEmpty():
            selectionRectPath = QPainterPath()
            selectionRectPath.addRect(selectionRect)
            path = self.__origDragMaskPath - selectionRectPath
            self.__dragMask.setPath(path)
            self.__dragMask.show()

            self.__selectionRectBorderItem.setRect(selectionRect.adjusted(-2, -2, 2, 2))
            self.__selectionRectBorderItem.show()
        else:
            self.__dragMask.hide()
            self.__selectionRectBorderItem.hide()

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if event.button() & Qt.MouseButton.LeftButton:
            self.__dragging = True
            self.__dragMask.show()
            self.__startScenePos = event.scenePos().toPoint()

        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if self.__dragging:
            currentScenePos = event.scenePos().toPoint()
            self.drawSelectionRect(self.calculateSelectionRect(currentScenePos))

        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        if event.button() & Qt.MouseButton.LeftButton and self.__dragging:
            self.__selectionRect = self.calculateSelectionRect(event.scenePos())
            self.selectionRectChangedByDrag.emit()
            self.__dragging = False

        return super().mouseReleaseEvent(event)


class ImageCropper(Ui_ImageCropper, QWidget):
    selectionRectChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.viewZoomWrapper = GraphicsViewZoomWrapper(self.graphicsView)

        self.scene = CropGraphicsScene(self)
        self.scene.viewSceneRectChanged.connect(
            lambda: self.graphicsView.setSceneRect(self.scene.viewSceneRect)
        )
        self.scene.selectionRectChanged.connect(self.selectionRectChanged)

        self.scene.selectionRectChangedByDrag.connect(self.updateSpinBoxes)

        self.topLeftPointTopSpinBox.valueChanged.connect(
            self.__setSelectionRectBySpinBoxes
        )
        self.topLeftPointLeftSpinBox.valueChanged.connect(
            self.__setSelectionRectBySpinBoxes
        )
        self.widthSpinBox.valueChanged.connect(self.__setSelectionRectBySpinBoxes)
        self.heightSpinBox.valueChanged.connect(self.__setSelectionRectBySpinBoxes)

    def setPixmap(self, pixmap: QPixmap):
        self.scene.setPixmap(pixmap)
        self.graphicsView.setScene(self.scene)
        self.graphicsView.setScene(self.scene)
        self.topLeftPointTopSpinBox.setMaximum(pixmap.height())
        self.topLeftPointLeftSpinBox.setMaximum(pixmap.width())
        self.widthSpinBox.setMaximum(pixmap.width())
        self.heightSpinBox.setMaximum(pixmap.height())

    def blockSpinBoxSignals(self, b: bool):
        self.topLeftPointTopSpinBox.blockSignals(b)
        self.topLeftPointLeftSpinBox.blockSignals(b)
        self.widthSpinBox.blockSignals(b)
        self.heightSpinBox.blockSignals(b)

    def updateSpinBoxes(self):
        self.blockSpinBoxSignals(True)
        rect = self.scene.selectionRect()
        self.topLeftPointTopSpinBox.setValue(rect.top())
        self.topLeftPointLeftSpinBox.setValue(rect.left())
        self.widthSpinBox.setValue(rect.width())
        self.heightSpinBox.setValue(rect.height())
        self.blockSpinBoxSignals(False)

    @Slot()
    def on_zoomInButton_clicked(self):
        self.viewZoomWrapper.zoom(1.1)

    @Slot()
    def on_zoomOutButton_clicked(self):
        self.viewZoomWrapper.zoom(0.9)

    def selectionRect(self):
        return self.scene.selectionRect()

    def __setSelectionRectBySpinBoxes(self):
        rect = QRect(
            self.topLeftPointLeftSpinBox.value(),
            self.topLeftPointTopSpinBox.value(),
            self.widthSpinBox.value(),
            self.heightSpinBox.value(),
        )

        self.setSelectionRect(rect)

    def setSelectionRect(self, rect: QRect):
        # TODO:
        # here we disconnect signals to prevent potential RecursionError,
        # need to find a better way emitting signals to prevent this.
        # and great thanks to Bing AI finding this issue.
        self.scene.selectionRectChanged.disconnect(self.selectionRectChanged)
        self.scene.setSelectionRect(rect)
        self.updateSpinBoxes()
        self.selectionRectChanged.emit()
        self.scene.selectionRectChanged.connect(self.selectionRectChanged)

    def selectionPixmap(self):
        return self.scene.selectionPixmap()
