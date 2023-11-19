from typing import Callable, Coroutine, Union, Mapping, Any
import asyncio

from .http import HttpServer
from .database import Database, DatabaseBuilder
from .websocket import SocketServer


class Server:
    def __init__(
        self, database: Database, http: HttpServer, websocket: SocketServer
    ) -> None:
        self.__http: HttpServer = http
        self.__websocket: SocketServer = websocket
        self.__database: Database = database
        self.__listeners: list[Callable[[None], None]] = []

    @property
    def http(self) -> HttpServer:
        return self.__http

    @property
    def websocket(self) -> SocketServer:
        return self.__websocket

    @property
    def database(self) -> Database:
        return self.__database

    def start(self, function: Callable[[None], None]) -> Callable[[None], None]:
        self.__listeners.append(function)

        return function

    def start_server(self) -> None:
        for function in self.__listeners:
            result: Union[Coroutine, None] = function()

            if isinstance(result, Coroutine):
                asyncio.run(result)


class ServerFactory:
    @classmethod
    def __create_http(cls, data: Mapping[str, Any]) -> HttpServer:
        server: HttpServer = HttpServer(
            host=data["host"],
            port=data["port"],
            secret_key=data.get("secret_key"),
            debug=data.get("debug") or False,
        )

        return server

    @classmethod
    def __create_websocket(cls, http_server: HttpServer) -> SocketServer:
        server: SocketServer = SocketServer(http_server)

        return server

    @classmethod
    def __create_database(cls, data: Mapping[str, Any]) -> Database:
        return (
            DatabaseBuilder()
            .set_host(data["host"])
            .set_port(data["port"])
            .set_dbname(data["dbname"])
            .set_credentials(data["username"], data["password"])
            .set_driver(data["driver"])
            .set_dialect(data["dialect"])
            .set_debug(data.get("debug") or False)
            .build()
        )

    @classmethod
    def create(cls, http: Mapping[str, Any], database: Mapping[str, Any]) -> Server:
        http_server: HttpServer = cls.__create_http(http)
        database_server: Database = cls.__create_database(database)
        websocket_server: SocketServer = cls.__create_websocket(http_server)

        return Server(database_server, http_server, websocket_server)
