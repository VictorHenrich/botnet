from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Mapping, Optional
from selenium.webdriver.remote.webdriver import WebDriver

from targets.web.dom import DOM, DOMSelector, DOMOperator
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
        operator: Mapping[str, Any]
    ) -> None:
        self.__selector: DataDOMSelector = DataDOMSelector(**selector)

        self.__operator: DataDOMOperator = DataDOMOperator(**operator)

    def __get_selection(self) -> DOMSelector:
        selection: AbstractDOMSelection = \
            DOMSelections.get_selection(self.__selector.type)

        return DOMSelector(selection, self.__selector.value)

    def __get_operation(self) -> DOMOperator:
        operation: AbstractDOMOperation = \
            DOMOperations.get_operation(self.__operator.type) \
            if self.__operator else None

        return DOMOperator(operation, self.__operator.param)

    def constructor(self, webdriver: WebDriver) -> DOM:
        selection: DOMSelector = self.__get_selection()
        operation: AbstractDOMOperation = self.__get_operation()

        return DOM(
            webdriver,
            selection,
            operation
        )



class DataAutomateBrowser:
    def __init__(
        self,
        link: str,
        browser: str,
        dom: list[Mapping[str, Any]] = []
    ) -> None:
        self.__link: str = link

        self.__webdriver: AbstractDrive = Drives.get_drive(browser)

        self.__dom: list[DataFactoryDOM] = [
            DataFactoryDOM(**d)
            for d in dom
        ]

    @property
    def link(self) -> str:
        return self.__link

    @property
    def webdriver(self) -> AbstractDrive:
        return self.__webdriver

    @property
    def dom(self) -> list[DataFactoryDOM]:
        return self.__dom

        
