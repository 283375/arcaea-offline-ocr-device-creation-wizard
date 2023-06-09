from typing import TypeVar, Generic
from PySide6.QtCore import QObject

from PySide6.QtGui import QImage

from cv2 import Mat
import numpy as np

T = TypeVar("T")


class Singleton(type, Generic[T]):
    _instance = None

    def __call__(cls, *args, **kwargs) -> T:
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class QObjectSingleton(type(QObject), Singleton):
    pass


def qImage2cvMat(qImg: QImage) -> Mat:
    # https://stackoverflow.com/a/18449977/16484891
    # CC BY-SA 4.0
    qImg = qImg.convertToFormat(QImage.Format.Format_RGB32)

    width = qImg.width()
    height = qImg.height()

    ptr = qImg.bits()
    arr = np.array(ptr).reshape(height, width, 4)
    return arr
