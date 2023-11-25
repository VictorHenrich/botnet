from typing import (
    Callable,
    Coroutine,
    Optional,
    Mapping,
    Any,
    List,
    Awaitable,
    Sequence,
    TypeAlias,
)
import asyncio
from threading import Thread

from .http import HttpServer
from .database import Database, DatabaseBuilder
from .websocket import SocketServer


CallFunctionType: TypeAlias = Callable[[], Optional[Awaitable]]


class Server:
    __http: HttpServer

    __websocket: SocketServer

    __database: Database

    __listeners: List[CallFunctionType] = []

    @classmethod
    def __create_http(cls, data: Mapping[str, Any]) -> None:
        http_server: HttpServer = HttpServer(
            host=data["host"],
            port=data["port"],
            secret_key=data.get("secret_key", ""),
            debug=data.get("debug") or False,
        )

        cls.__http = http_server

        cls.__websocket = SocketServer(http_server)

    @classmethod
    def __create_database(cls, data: Mapping[str, Any]) -> None:
        cls.__database = (
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
    def init_app(cls, http: Mapping[str, Any], database: Mapping[str, Any]) -> None:
        cls.__create_http(http)
        cls.__create_database(database)

    @classmethod
    @property
    def http(cls) -> HttpServer:
        return cls.__http

    @classmethod
    @property
    def websocket(cls) -> SocketServer:
        return cls.__websocket

    @classmethod
    @property
    def database(cls) -> Database:
        return cls.__database

    @classmethod
    def start(cls, function: Callable[[], None]) -> Callable[[], None]:
        cls.__listeners.append(function)

        return function

    @classmethod
    def __handle_function(
        cls, function: CallFunctionType, event_loop: asyncio.AbstractEventLoop
    ) -> None:
        result: Optional[Awaitable] = function()

        if isinstance(result, Coroutine):
            event_loop.run_until_complete(result)

    @classmethod
    def start_app(cls) -> None:
        event_loop: asyncio.AbstractEventLoop = asyncio.get_event_loop()

        threads: Sequence[Thread] = [
            Thread(target=cls.__handle_function, args=(function, event_loop))
            for function in cls.__listeners
        ]

        [thread.start() for thread in threads]

        [thread.join() for thread in threads]
