from __future__ import annotations
from pathlib import Path
from typing import Any, Mapping, Union
from pydantic import BaseModel, validator, validate_arguments
from selenium.webdriver.remote.webdriver import WebDriver
from dataclasses import dataclass

from targets.web.dom import DOM, DOMSelector, DOMOperator, AbstractDOM
from targets.web.dom.operation import AbstractDOMOperation, DOMOperations
from targets.web.dom.selection import AbstractDOMSelection, DOMSelections
from targets.web.drives import Drives, AbstractDrive


@dataclass
class DataDOMSelector:
    type: str
    value: str


@dataclass
class DataDOMOperator:
    type: str
    param: Any


class DataFactoryDOM:
    def __init__(
        self,
        selector: Mapping[str, str],
        operator: Mapping[str, Any],
        wait_time: float = 0
    ) -> None:
        self.__selector: DataDOMSelector = DataDOMSelector(**selector)
        self.__operator: DataDOMOperator = DataDOMOperator(**operator)
        self.__wait_time: float = wait_time

    @property
    def selector(self) -> DataDOMSelector:
        return self.__selector

    @property
    def operator(self) -> DataDOMOperator:
        return self.__operator

    @property
    def wait_time(self) -> float:
        return self.__wait_time

    def __get_selection(self) -> DOMSelector:
        selection: AbstractDOMSelection = \
            DOMSelections.get_selection(self.__selector.type)

        return DOMSelector(selection, self.__selector.value)

    def __get_operation(self) -> DOMOperator:
        operation: AbstractDOMOperation = \
            DOMOperations.get_operation(self.__operator.type) \
            if self.__operator else None

        return DOMOperator(operation, self.__operator.param)

    def constructor_dom(self, webdriver: WebDriver) -> DOM:
        selection: DOMSelector = self.__get_selection()
        operation: AbstractDOMOperation = self.__get_operation()

        return DOM(
            webdriver,
            selection,
            operation,
            self.__wait_time
        )



class DataAutomateBrowser(AbstractDOM):
    def __init__(
        self,
        browser: str,
        dom: list[Mapping[str, Any]],
        link: str
    ) -> None:
        self.__webdriver: AbstractDrive = Drives.get_drive(browser)

        self.__dom: list[DataFactoryDOM] = [
            DataFactoryDOM(**d)
            for d in dom
        ]

        self.__link: str = link

    @property
    def webdriver(self) -> AbstractDrive:
        return self.__webdriver

    @property
    def dom(self) -> list[DataFactoryDOM]:
        return self.__dom

    @property
    def link(self) -> str:
        return self.__link

    def active(self, path_drive: Union[Path, str]) -> None:
        path_drive_: str = str(path_drive)

        driver_browser: WebDriver = self.__webdriver.get_browser(path_drive_)

        driver_browser.get(self.__link)

        for d in self.__dom:
            d \
                .constructor_dom(driver_browser) \
                .active()

        
