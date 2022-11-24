from typing import Type, Mapping, Optional
from dataclasses import dataclass
import pyautogui
from time import sleep

from start import client
from client.managers import Task
from client.utils import UtilEnv


env_value: Mapping[str, Optional[str]] = UtilEnv.get_values()



@dataclass
class DataAutomateNotepad:
    text: str



@client.managers.add_task(env_value['MANAGER_AUTOMATE_SO'])
class OpenNotepad(Task):
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

