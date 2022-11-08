from typing import  Type
from pathlib import Path

from start import client
from services.managers.target_manager import TargetManager
from .utils.data_class_runbrowser import DataAutomateBrowser




class RunBrowser(TargetManager):
    name: str = "abrir_pagina"
    data_class: Type = DataAutomateBrowser
    debug: bool = False

    __executable_path_default_browser, = Path().cwd().glob('**/webdrives')

    def execute(self, data: DataAutomateBrowser):
        path_browser: str = str(RunBrowser.__executable_path_default_browser / data.webdriver.name_executable)

        data.active(path_browser)



client.managers.get_manager('automacao_navegador').append_targets(RunBrowser)