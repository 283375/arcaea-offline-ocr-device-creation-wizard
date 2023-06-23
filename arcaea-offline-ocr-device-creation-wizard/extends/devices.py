from dataclasses import asdict
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


def write_devices_json(filepath: str, devices: list[Device]):
    with open(filepath, "r+", encoding="utf-8") as f:
        f.truncate(0)
        f.write(
            json.dumps(
                [asdict(device) for device in devices], indent=2, ensure_ascii=False
            )
        )


def qRect_to_device_rect(rect: QRect):
    return (rect.left(), rect.top(), rect.width(), rect.height())
