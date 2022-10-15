from typing import  Type
from pathlib import Path

from services import client
from services.managers.manager_target import ManagerTarget
from .utils.data_class_runbrowser import DataAutomateBrowser




class RunBrowser(ManagerTarget):
    name: str = "abrir_pagina"
    data_class: Type = DataAutomateBrowser
    debug: bool = False

    __executable_path_default_browser, = Path().cwd().glob('**/webdrives')

    def execute(self, data: DataAutomateBrowser):
        path_browser: str = str(RunBrowser.__executable_path_default_browser / data.webdriver.name_executable)

        with data.webdriver.get_browser(path_browser) as browser:
            browser.get(data.link)

            if data.dom:
                data.dom.constructor(browser).activate()



client.manager_main.get_manager('automacao_navegador').append_targets(RunBrowser)