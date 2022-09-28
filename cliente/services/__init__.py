from .configs import (
    __URL_SOCKET__,
    __MANAGERS__
)

from .client.server_client import ServerClient
from .utils.create_server_client import create_server_client


server_client: ServerClient = create_server_client(__URL_SOCKET__, __MANAGERS__)
