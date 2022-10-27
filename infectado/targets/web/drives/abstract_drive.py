from abc import ABC
from pathlib import Path
from typing import Union, Type, Union
from selenium.webdriver.remote.webdriver import WebDriver



class AbstractDrive(ABC):
    name_executable: Union[Path, str]
    name: str
    class_: Type[WebDriver]