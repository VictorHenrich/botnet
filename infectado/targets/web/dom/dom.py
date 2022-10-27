from __future__ import annotations
from typing import Any, Optional
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from . import (
    AbstractDOMSelection,
    AbstractDOMOperation,
    DOMOperations,
    DOMSelections
)


class DOM:
    def __init__(
        self,
        webdriver: WebDriver,
        selector_type: str,
        selector_value: str,
        operator_type: str,
        operator_value: Any,
        next_dom: Optional[DOM]
    ) -> None:
        self.__selector_type: AbstractDOMSelection = DOMSelections.get_selection(selector_type)
        self.__operator_type: AbstractDOMOperation = DOMOperations.get_operation(operator_type)

        self.__selector_value: str = selector_value
        self.__operator_value: Any = operator_value

        self.__webdriver: WebDriver = webdriver
        self.__next: Optional[DOM] = next_dom


    def execute(self) -> None:
        element: WebElement = self.__selector_type.get_by(self.__webdriver, self.__selector_value)

        if not element:
            raise Exception('Element DOM not localized!')

        self.__operator_type.operate(element or self.__webdriver, self.__operator_value)

        if self.__next:
            self.__next.execute()