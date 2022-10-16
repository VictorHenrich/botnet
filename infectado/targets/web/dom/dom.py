from __future__ import annotations
from typing import Any, Optional, Sequence, Mapping
from dataclasses import dataclass
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from . import (
    AbstractDOMSelection,
    AbstractDOMOperation
)




@dataclass
class DOMSelector:
    type: AbstractDOMSelection
    value: str



@dataclass
class DOMOperator:
    type: AbstractDOMOperation
    param: Any


class DOM:
    def __init__(
        self,
        webdriver: WebDriver,
        selector: DOMSelector,
        operator: DOMOperator
    ) -> None:
        self.__webdriver: WebDriver = webdriver
        self.__selector: DOMSelector = selector
        self.__operator: DOMOperator = operator

    
    def activate(self) -> None:
        element: WebElement = \
            self.__selector \
                .type \
                .get_by(self.__webdriver, self.__selector.value)

        self.__operator\
            .type\
            .start(
                self.__webdriver,
                element,
                self.__operator.param
            )

        


    