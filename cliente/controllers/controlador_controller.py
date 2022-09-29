from services import client
from services.websocket import Controller



class ControladorController(Controller):
    name: str = "escutar_controlador"

    async def on_connect(self) -> None:
        pass

    async def on_disconnect(self) -> None:
        pass

    async def on_control(self, data) -> None:
        pass



client.websocket.register_controller(ControladorController)




