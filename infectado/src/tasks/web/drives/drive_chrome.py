from typing import Type, Union
from pathlib import Path
from selenium.webdriver import Chrome

from .abstract_drive import AbstractDrive
from .drives import Drives


class DriveChrome(AbstractDrive):
    name_executable = "chromedriver.exe"
    name = "chrome"
    class_ = Chrome


Drives.append_drive(DriveChrome)
