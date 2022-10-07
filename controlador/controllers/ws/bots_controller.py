from services import server
from services.websocket import Controller


@server.websocket.on('/bots')
class BotsController(Controller):
    pass