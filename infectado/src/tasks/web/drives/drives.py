from typing import Mapping
from .abstract_drive import AbstractDrive


class Drives:
    __mapping_drives: Mapping[str, AbstractDrive] = {}

    @classmethod
    def append_drive(cls, drive: AbstractDrive) -> None:
        cls.__mapping_drives[drive.name] = drive

    @classmethod
    def get_drive(cls, name: str) -> AbstractDrive:
        try:
            return cls.__mapping_drives[name]
        except KeyError:
            raise ValueError("Drive não localizado!")
