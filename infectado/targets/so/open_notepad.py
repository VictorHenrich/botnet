from typing import Any, Mapping, Type
from dataclasses import dataclass
import pyautogui

from services.managers import ManagerTarget


@dataclass
class DataAutomateNotepad:
    text: str


class OpenNotepad(ManagerTarget):
    name: str = "rodar_navegador"
    debug: bool = False
    data_class: Type = DataAutomateNotepad

    def execute(self, data: DataAutomateNotepad) -> None:
        pass