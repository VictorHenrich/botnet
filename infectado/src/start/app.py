from .configs import (
    __MANAGERS__,
    __SOCKET__
)
from services import ClientFactory, Client



client: Client = ClientFactory.create(__MANAGERS__, __SOCKET__)