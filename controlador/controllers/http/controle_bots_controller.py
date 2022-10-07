from typing import Any, Mapping, Optional
from dataclasses import dataclass

from services import server
from services.http import (
    Controller,
    ResponseFailure,
    ResponseSuccess,
    Response
)
from middlewares import (
   AutenticacaoMiddlware,
   ValidacaoCorpoRequisicaoMiddleware
)
from models import Usuarios



@dataclass
class ModelControle:
    module: str
    targets: list[str]
    args: Optional[Mapping[str, Any]] = None



@server.http.routes.view('/controlar')
class ControleBotsController(Controller):

    @AutenticacaoMiddlware.apply()
    @ValidacaoCorpoRequisicaoMiddleware.apply(ModelControle)
    async def post(self, auth: Usuarios, body_request: ModelControle) -> Response:
        try:
            await server.websocket.socket.emit('on_controller', body_request.__dict__)

        except Exception as error:
            return ResponseFailure(data=str(error))

        else:
            return ResponseSuccess()





