from services.http.server_http import ServerHttp
from services.websocket.server_socket import ServerSocket
from services.server import Server


def create_server(
    host: str,
    port: int,
    debug: bool
) -> Server:
    http: ServerHttp = \
        ServerHttp(
            host,
            port,
            debug
        )

    websocket: ServerSocket = ServerSocket(http)

    return Server(
        http,
        websocket
    )