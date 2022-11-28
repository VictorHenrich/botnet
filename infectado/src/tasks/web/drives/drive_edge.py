from typing import Type, Union
from pathlib import Path
from selenium.webdriver import Edge

from .abstract_drive import AbstractDrive
from .drives import Drives



class DriveEdge(AbstractDrive):
    name_executable = "msedgedriver.exe"
    name = "edge"
    class_ = Edge
    

Drives.append_drive(DriveEdge)
