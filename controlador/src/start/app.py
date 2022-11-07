from services import Server, ServerFactory
from .configs import (
    __DATABASE__,
    __HTTP__
)




server: Server = ServerFactory.create(__HTTP__, __DATABASE__)