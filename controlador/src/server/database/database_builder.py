from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Union
import urllib.parse
from .database import Database


@dataclass
class DatabaseBuilder:
    dialect: str = ""
    host: Optional[str] = None
    port: Optional[Union[str, int]] = None
    dbname: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    driver: Optional[str] = None
    debug: bool = False

    def set_dialect(self, dialect: str) -> DatabaseBuilder:
        self.dialect = dialect

        return self

    def set_host(self, host: str) -> DatabaseBuilder:
        self.host = host

        return self

    def set_port(self, port: Union[str, int]) -> DatabaseBuilder:
        self.port = port

        return self

    def set_dbname(self, dbname: str) -> DatabaseBuilder:
        self.dbname = dbname

        return self

    def set_credentials(self, username: str, password: str) -> DatabaseBuilder:
        self.username = username
        self.password = urllib.parse.quote_plus(password)

        return self

    def set_driver(self, driver: str) -> DatabaseBuilder:
        self.driver = driver

        return self

    def set_debug(self, debug: bool) -> DatabaseBuilder:
        self.debug = debug

        return self

    def build(self) -> Database:
        url: str = f"{self.dialect}+{self.driver}://{self.username}:{self.password}@{self.host}:{self.port}/{self.dbname}"

        return Database(url, self.debug)
