from typing import Generic, TypeVar

from cv2 import Mat
from numpy import frombuffer as np_frombuffer
from numpy import uint8
from PySide6.QtCore import QObject
from PySide6.QtGui import QImage

T = TypeVar("T")


class Singleton(type, Generic[T]):
    _instance = None

    def __call__(cls, *args, **kwargs) -> T:
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class QObjectSingleton(type(QObject), Singleton):
    pass


def qImage2cvMatRGBA(qImg: QImage) -> Mat:
    # from Bing AI, references
    # 1: https://stackoverflow.com/q/384759/16484891 | CC BY-SA 4.0
    # 2: https://stackoverflow.com/q/37552924/16484891 | CC BY-SA 3.0
    qImg = qImg.convertToFormat(QImage.Format.Format_RGBA8888)
    qImg_data = qImg.constBits()
    np_arr = np_frombuffer(qImg_data, uint8)
    return np_arr.reshape((qImg.height(), qImg.width(), 4))
