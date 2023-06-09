from PySide6.QtWidgets import QGraphicsView
from PySide6.QtCore import QPointF


class GraphicsViewZoomWrapper(QGraphicsView):
    """
    Ported from https://stackoverflow.com/a/19114517/16484891
    CC BY-SA 3.0
    """

    def __init__(self, view: QGraphicsView):
        self.__view = view
        self.target_scene_pos = QPointF()
        self.target_viewport_pos = QPointF()

    def setView(self, view: QGraphicsView):
        self.__view = view

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
