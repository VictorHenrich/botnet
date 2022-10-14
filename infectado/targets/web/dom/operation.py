from abc import ABC, abstractmethod
from typing import Any, Mapping, Type
from selenium.webdriver.remote.webelement import WebElement



class AbstractDOMOperation(ABC):
    name: str

    def __init__(self) -> None:
        operator_name: str = self.__class__.name

        if type(operator_name) is not str:
            raise Exception('Operator name is invalid or undefined!')

    @abstractmethod
    def operate(self, web_element: WebElement, param: Any) -> None:
        pass



class DOMOperations:
    __mapped_operations: Mapping[str, AbstractDOMOperation] = {}

    @classmethod
    def insert_operation(cls, operation: Type[AbstractDOMOperation]) -> None:
        cls.__mapped_operations[operation.name] = operation()

    @classmethod
    def get_operation(cls, name: str) -> AbstractDOMOperation:
        return cls.__mapped_operations[name]