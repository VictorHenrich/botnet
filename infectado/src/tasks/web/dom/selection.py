from abc import ABC, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import Mapping, Type, Union


class AbstractDOMSelection(ABC):
    name: str

    def __init__(self) -> None:
        selection_name: str = self.__class__.name

        if type(selection_name) is not str:
            raise Exception("Operator name is invalid or undefined!")

    @abstractmethod
    def get_by(self, web: Union[WebDriver, WebElement], identifier: str) -> WebElement:
        pass


class DOMSelections:
    __mapped_selections: Mapping[str, AbstractDOMSelection] = {}

    @classmethod
    def insert_selection(cls, selection: Type[AbstractDOMSelection]) -> None:
        cls.__mapped_selections[selection.name] = selection()

    @classmethod
    def get_selection(cls, name: str) -> AbstractDOMSelection:
        return cls.__mapped_selections[name]
