from PySide6.QtCore import QEvent, QObject, QPointF, Qt
from PySide6.QtGui import QMouseEvent, QWheelEvent
from PySide6.QtWidgets import QApplication, QGraphicsView


class GraphicsViewZoomWrapper(QObject):
    """
    Ported from https://stackoverflow.com/a/19114517/16484891
    CC BY-SA 3.0
    """

    def __init__(self, view: QGraphicsView):
        super().__init__(view)
        self.target_scene_pos = QPointF()
        self.target_viewport_pos = QPointF()

        self.__modifier = Qt.KeyboardModifier.ControlModifier
        self.__zoom_factor_base = 1.0015

        view.viewport().installEventFilter(self)
        view.setMouseTracking(True)
        self.__view = view

    def setModifier(self, modifier: Qt.KeyboardModifier):
        self.__modifier = modifier

    def zoom(self, factor: float):
        target_scene_pos = QPointF(
            (
                self.__view.mapToScene(self.__view.viewport().rect().center())
                if self.target_scene_pos.isNull()
                else self.target_scene_pos
            )
        )
        target_viewport_pos = QPointF(
            (
                self.__view.viewport().rect().center()
                if self.target_viewport_pos.isNull()
                else self.target_viewport_pos
            )
        )

        self.__view.scale(factor, factor)
        self.__view.centerOn(target_scene_pos)
        delta_viewport_pos = target_viewport_pos - QPointF(
            self.__view.viewport().width() / 2.0, self.__view.viewport().height() / 2.0
        )
        viewport_center = (
            QPointF(self.__view.mapFromScene(target_scene_pos)) - delta_viewport_pos
        )
        self.__view.centerOn(self.__view.mapToScene(viewport_center.toPoint()))

    def zoomIn(self):
        self.zoom(1.05)

    def zoomOut(self):
        self.zoom(0.95)

    def eventFilter(self, object: QObject, event: QEvent):
        if isinstance(event, QMouseEvent):
            delta = QPointF(self.target_viewport_pos - event.pos())
            if abs(delta.x()) > 5 or abs(delta.y()) > 5:
                self.target_viewport_pos = event.pos()
                self.target_scene_pos = self.__view.mapToScene(event.pos())
        elif isinstance(event, QWheelEvent):
            if (
                QApplication.keyboardModifiers() == self.__modifier
                and abs(event.angleDelta().y()) > 0
            ):
                angle = event.angleDelta().y()
                factor = pow(self.__zoom_factor_base, angle)
                self.zoom(factor)
                return True

        return False
