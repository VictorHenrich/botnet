from __future__ import annotations
from pathlib import Path
from typing import Any, Mapping, Union
from pydantic import BaseModel, validator, validate_arguments
from selenium.webdriver.remote.webdriver import WebDriver

from targets.web.dom import DOM, DOMSelector, DOMOperator, AbstractDOM
from targets.web.dom.operation import AbstractDOMOperation, DOMOperations
from targets.web.dom.selection import AbstractDOMSelection, DOMSelections
from targets.web.drives import Drives, AbstractDrive



class DataDOMSelector(BaseModel):
    type: str
    value: str



class DataDOMOperator(BaseModel):
    type: str
    param: Any


class DataFactoryDOM(BaseModel):
    selector: DataDOMSelector
    operator: DataDOMOperator


    @validator('selector', pre=True)
    def handle_data_selector(cls, value: Mapping[str, str]) -> DataDOMSelector:
        return DataDOMSelector(**value)

    @validator('operator', pre=True)
    def handle_data_operator(cls, value: Mapping[str, Any]) -> DataDOMOperator:
        return DataDOMOperator(**value)

    def __get_selection(self) -> DOMSelector:
        selection: AbstractDOMSelection = \
            DOMSelections.get_selection(self.selector.type)

        return DOMSelector(selection, self.selector.value)

    def __get_operation(self) -> DOMOperator:
        operation: AbstractDOMOperation = \
            DOMOperations.get_operation(self.operator.type) \
            if self.operator else None

        return DOMOperator(operation, self.operator.param)

    def constructor_dom(self, webdriver: WebDriver) -> DOM:
        selection: DOMSelector = self.__get_selection()
        operation: AbstractDOMOperation = self.__get_operation()

        return DOM(
            webdriver,
            selection,
            operation
        )



class DataAutomateBrowser(AbstractDOM, BaseModel):
    link: str
    browser: AbstractDrive
    dom: list[DataFactoryDOM] = []


    @validator('browser', pre=True)
    def handle_browser(cls, value: str) -> AbstractDrive:
        return Drives.get_drive(value)

    @validator('dom', pre=True)
    def handle_dom(cls, value: list[Mapping[str, Any]]) -> list[DataFactoryDOM]:
        return [
            DataFactoryDOM(**dom)
            for dom in value
        ]

    @validate_arguments
    def active(self, path_drive: Union[Path, str]) -> None:
        path_drive_: str = str(path_drive)

        driver_browser: WebDriver = self.browser.get_browser(path_drive_)

        driver_browser.get(self.link)

        for d in self.dom:
            d \
                .constructor_dom(driver_browser) \
                .active()

        
