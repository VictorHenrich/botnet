from dataclasses import dataclass
from typing import Type
from selenium.webdriver import Edge
from pathlib import Path

from services import client
from services.managers.manager_target import ManagerTarget



@dataclass
class DataAutomateBrowser:
    link: str


class RunBrowser(ManagerTarget):
    name: str = "abrir_pagina"
    data_class: Type = DataAutomateBrowser
    debug: bool = False

    __executable_browser: str = str(Path().cwd() / 'targets' / 'web' / 'drives' / 'msedgedriver.exe')

    def execute(self, data: DataAutomateBrowser):
        with Edge(RunBrowser.__executable_browser) as browser:
            browser.get(data.link)



client.manager_main.get_manager('automacao_navegador').append_targets(RunBrowser)