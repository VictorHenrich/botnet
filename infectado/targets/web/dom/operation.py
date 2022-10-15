from abc import ABC, abstractmethod
from typing import Any, Mapping, Optional, Sequence, Type
from selenium.webdriver.remote.webelement import WebElement



class AbstractDOMOperation(ABC):
    name: str
    parameter_type: Optional[Type[Any]] = None

    def __init__(self) -> None:
        operator_name: str = self.__class__.name

        if type(operator_name) is not str:
            raise Exception('Operator name is invalid or undefined!')

    @abstractmethod
    def operate(self, web_element: WebElement, param: Any) -> None:
        pass

    def start(self, web_element: WebElement, param: Any) -> None:
        parameter_class: Type[Any] = self.__class__.parameter_type

        if parameter_class and isinstance(param, parameter_class):
            if type(param) is Mapping:
                self.operate(web_element, parameter_class(**param))
                return

            elif type(param) is Sequence:
                self.operate(web_element, parameter_class(*param))
                return

            else:
                self.operate(web_element, param)
                return

        self.operate(web_element, param)





class DOMOperations:
    __mapped_operations: Mapping[str, AbstractDOMOperation] = {}

    @classmethod
    def insert_operation(cls, operation: Type[AbstractDOMOperation]) -> None:
        cls.__mapped_operations[operation.name] = operation()

    @classmethod
    def get_operation(cls, name: str) -> AbstractDOMOperation:
        return cls.__mapped_operations[name]