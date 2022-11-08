from typing import Type
from dataclasses import dataclass
import pyautogui
from time import sleep

from start import client
from services.managers import TargetManager


@dataclass
class DataAutomateNotepad:
    text: str


class OpenNotepad(TargetManager):
    name: str = "abrir_bloco_notas"
    debug: bool = False
    data_class: Type = DataAutomateNotepad

    def execute(self, data: DataAutomateNotepad) -> None:
        pyautogui.press('win')
        pyautogui.write('notepad')
        pyautogui.press('enter')

        sleep(2)
        
        for letter in data.text:
            pyautogui.press(letter)
            sleep(0.05)



client.managers.get_manager('automacao_so').append_targets(OpenNotepad)

