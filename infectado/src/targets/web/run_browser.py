from typing import  Type
from pathlib import Path

from services import client
from infectado.src.services.managers.target_manager import TargetManager
from .utils.data_class_runbrowser import DataAutomateBrowser




class RunBrowser(TargetManager):
    name: str = "abrir_pagina"
    data_class: Type = DataAutomateBrowser
    debug: bool = False

    __executable_path_default_browser, = Path().cwd().glob('**/webdrives')

    def execute(self, data: DataAutomateBrowser):
        path_browser: str = str(RunBrowser.__executable_path_default_browser / data.webdriver.name_executable)

        data.active(path_browser)



client.manager_main.get_manager('automacao_navegador').append_targets(RunBrowser)