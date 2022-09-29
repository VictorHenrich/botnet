from typing import Union
from pathlib import Path

from services.http.server_http import ServerHttp
from services.websocket.server_socket import ServerSocket
from services.database import Database
from services.server import Server


def create_server(
    host: str,
    port: int,
    secret_key: str,
    url_database: Union[Path, str],
    debug: bool
) -> Server:
    http: ServerHttp = \
        ServerHttp(
            host,
            port,
            secret_key,
            debug
        )

    database: Database = Database(url_database, debug)

    websocket: ServerSocket = ServerSocket(http)

    return Server(
        database,
        http,
        websocket
    )