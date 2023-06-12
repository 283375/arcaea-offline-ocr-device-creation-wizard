import json

from arcaea_offline_ocr.device import Device
from PySide6.QtCore import QRect


def load_devices_json(filepath: str) -> list[Device]:
    with open(filepath, "r", encoding="utf-8") as f:
        file_content = f.read()
        if len(file_content) == 0:
            return []
        content = json.loads(file_content)
        assert isinstance(content, list)
        return [Device.from_json_object(item) for item in content]


def qRect_to_device_rect(rect: QRect) :
    return (rect.left(), rect.top(), rect.width(), rect.height())
