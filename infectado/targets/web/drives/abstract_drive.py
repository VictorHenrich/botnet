from abc import ABC
from pathlib import Path
from typing import Union, Type, Union
from selenium.webdriver import (
    Chrome,
    Edge,
    Safari,
    Firefox
)



class AbstractDrive(ABC):
    name_executable: Union[Path, str]
    name: str
    class_: Type[Union[Chrome, Edge, Safari, Firefox]]