from dataclasses import dataclass
from typing import Any, Mapping, Optional, Type
from pathlib import Path

from services import client
from services.managers.manager_target import ManagerTarget
from targets.web.dom import DOM
from .drives import Drives, AbstractDrive


@dataclass
class DataAutomateBrowser:
    link: str
    browser: str
    dom: Optional[Mapping[str, Any]] = None



class RunBrowser(ManagerTarget):
    name: str = "abrir_pagina"
    data_class: Type = DataAutomateBrowser
    debug: bool = False

    __executable_path_default_browser, = Path().cwd().glob('**/webdrives')

    def execute(self, data: DataAutomateBrowser):
        object_drive: AbstractDrive = Drives.get_drive(data.browser)
        
        path_browser: str = str(RunBrowser.__executable_path_default_browser / object_drive.name_executable)

        with object_drive.class_(path_browser) as browser:
            browser.get(data.link)

            if data.dom:
                dom: DOM = DOM(**data.dom)

                dom.execute()



client.manager_main.get_manager('automacao_navegador').append_targets(RunBrowser)