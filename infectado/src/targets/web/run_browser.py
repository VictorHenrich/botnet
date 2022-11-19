from typing import  Type, Mapping, Optional
from pathlib import Path

from start import client
from services.managers.target_manager import TargetManager
from .utils.data_class_runbrowser import DataAutomateBrowser
from services.utils import UtilEnv


env_value: Mapping[str, Optional[str]] = UtilEnv.get_values()


class RunBrowser(TargetManager):
    name: str = "abrir_pagina"
    data_class: Type = DataAutomateBrowser
    debug: bool = False

    __executable_path_default_browser, = list(Path.cwd().glob('**/webdrives'))

    def execute(self, data: DataAutomateBrowser):
        path_browser: str = str(RunBrowser.__executable_path_default_browser / data.webdriver.name_executable)

        data.active(path_browser)



client\
    .managers\
    .get_manager(env_value['MANAGER_AUTOMATE_BROWSER'])\
    .append_targets(RunBrowser)