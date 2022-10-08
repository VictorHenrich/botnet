from .configs import (
    __URL_SOCKET__,
    __MANAGERS__,
    __NAMESPACES__
)

from .client import Client
from .utils.create_client import create_client


client: Client = create_client(__URL_SOCKET__, __MANAGERS__, __NAMESPACES__)
