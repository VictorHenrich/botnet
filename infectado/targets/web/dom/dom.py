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



@dataclass
class DOMOptions:
    run_first_main: bool = False
    wait_elements: int = 10


class DOM:
    def __init__(
        self,
        webdriver: WebDriver,
        selector: DOMSelector,
        operator: Optional[DOMOperator] = None,
        *children: Sequence[DOM],
        **options: Mapping[str, Any]
    ) -> None:
        self.__webdriver: WebDriver = webdriver
        self.__selector: DOMSelector = selector
        self.__operator: DOMOperator = operator
        self.__children: list[DOM] = list(children)
        self.__options: DOMOptions = DOMOptions(**options)

    def __run_children(self):
        for child in self.__children:
            child.activate()

    def __run_operator(self, element: Optional[WebElement]) -> None:
        if self.__operator:
            self.__operator\
                .type\
                .operate(
                    element or self.__webdriver, 
                    self.__operator.param
                )

    def activate(self) -> None:
        #self.__webdriver.implicitly_wait(self.__options.wait_elements)

        element: WebElement = \
            self.__selector \
                .type \
                .get_by(self.__webdriver, self.__selector.value)

        if self.__options.run_first_main:
            self.__run_operator(element)
            self.__run_children()

        else:
            self.__run_children()
            self.__run_operator(element)

        


    