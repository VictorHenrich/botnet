from .utils.create_server import create_server
from .server import Server
from .configs import (
    __DEBUG__,
    __HOST__,
    __PORT__
)


server: Server = create_server(
    __HOST__,
    __PORT__,
    __DEBUG__
)
