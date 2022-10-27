from __future__ import annotations
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


@dataclass
class DataDOMSelector:
    type: str
    value: str


@dataclass
class DataDOMOperator:
    type: str
    param: Any


class DataDOM:
    def __init__(
        self, 
        operator: Mapping[str, Any], 
        selector: Mapping[str, str],
        next: Optional[Mapping[str, Any]] = None
    ) -> None:
        self.__operator: DataDOMOperator = DataDOMOperator(**operator)
        self.__selector: DataDOMSelector = DataDOMSelector(**selector)
        self.__next: Optional[DataDOM] = DataDOM(**next) if next else None

    @property
    def operator(self) -> DataDOMOperator:
        return self.__operator

    @property
    def selector(self) -> DataDOMSelector:
        return self.__selector

    @property
    def next(self) -> Optional[DataDOM]:
        return self.__next






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
                data_dom: DataDOM = DataDOM(**data.dom)

                DOM(
                    webdriver=browser,
                    selector_type=data_dom.selector.type,
                    selector_value=data_dom.selector.value,
                    operator_type=data_dom.operator.type,
                    operator_value=data_dom.operator.param,
                    next_dom=data_dom.next
                ).execute()



client.manager_main.get_manager('automacao_navegador').append_targets(RunBrowser)