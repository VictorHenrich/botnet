from typing import  Type, Mapping, Optional
from pathlib import Path

from start import client
from client.managers.task import Task
from .utils.data_class_runbrowser import DataAutomateBrowser
from client.utils import UtilEnv


env_value: Mapping[str, Optional[str]] = UtilEnv.get_values()



@client.managers.add_task(env_value['MANAGER_AUTOMATE_BROWSER'])
class RunBrowser(Task):
    name: str = "abrir_pagina"
    data_class: Type = DataAutomateBrowser
    debug: bool = False

    __executable_path_default_browser, = list(Path.cwd().glob('**/webdrives'))

    def execute(self, data: DataAutomateBrowser):
        path_browser: str = str(RunBrowser.__executable_path_default_browser / data.webdriver.name_executable)

        data.active(path_browser)
