from .configs import __MANAGERS__, __SOCKET__
from client import ClientFactory, Client


client: Client = ClientFactory.create(__MANAGERS__, __SOCKET__)
