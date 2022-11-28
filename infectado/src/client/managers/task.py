
from typing import Any, Optional, Type
from .abstract_command import AbstractCommand
from abc import ABC, abstractmethod




class Task(AbstractCommand, ABC):
    name: str
    debug: bool = False
    data_class: Optional[Type] = None

    def __init__(self) -> None:
        if not self.__class__.name:
            raise Exception(f"Class {self.__class__.__name__} no name has been defined")

    @property
    def name(self) -> str:
        return self.__class__.name

    @property
    def debug(self) -> bool:
        return self.__class__.debug

    @property
    def data_class(self) -> Optional[Type]:
        return self.__class__.data_class

    @abstractmethod
    def execute(self, data: Optional[Any]) -> None:
        pass