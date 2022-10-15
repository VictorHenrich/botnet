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
        operator: Optional[Mapping[str, Any]] = None, 
        children: Optional[list[Mapping[str, Any]]] = None
    ) -> None:
        self.__selector: DataDOMSelector = DataDOMSelector(**selector)

        self.__operator: Optional[DataDOMOperator] = \
            DataDOMOperator(**operator) \
            if operator else None

        self.__children: Optional[list[DataFactoryDOM]] = \
            [
                DataFactoryDOM(**child)
                for child in children or []
            ]

    def __get_selection(self) -> DOMSelector:
        selection: AbstractDOMSelection = \
            DOMSelections.get_selection(self.__selector.type)

        return DOMSelector(selection, self.__selector.value)

    def __get_operation(self) -> Optional[DOMOperator]:
        if not self.__operator:
            return None

        operation: AbstractDOMOperation = \
            DOMOperations.get_operation(self.__operator.type) \
            if self.__operator else None

        return DOMOperator(operation, self.__operator.param)

    def constructor(self, webdriver: WebDriver) -> DOM:
        selector: DOMSelector = self.__get_selection()
        operator: Optional[DOMOperator] = self.__get_operation()

        children: list[DOM] = [
            child.constructor(webdriver)
            for child in self.__children
        ]

        return DOM(
            webdriver,
            selector,
            operator,
            *children
        )



class DataAutomateBrowser:
    def __init__(
        self,
        link: str,
        browser: str,
        dom: Optional[Mapping[str, Any]] = None
    ) -> None:
        self.__link: str = link
        self.__webdriver: AbstractDrive = Drives.get_drive(browser)
        self.__dom: Optional[DataFactoryDOM] = DataFactoryDOM(**dom) if dom else None

    @property
    def link(self) -> str:
        return self.__link

    @property
    def webdriver(self) -> AbstractDrive:
        return self.__webdriver

    @property
    def dom(self) -> Optional[DataFactoryDOM]:
        return self.__dom

        
