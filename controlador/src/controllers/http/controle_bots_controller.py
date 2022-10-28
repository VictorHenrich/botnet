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
from .bases import Controle as BaseControle



@server.http.routes.view('/controlar')
class ControleBotsController(Controller):

    @AutenticacaoMiddlware.apply()
    @ValidacaoCorpoRequisicaoMiddleware.apply(BaseControle)
    async def post(self, auth: Usuarios, body_request: BaseControle) -> Response:
        try:
            await server.websocket.socket.emit('controle', body_request.__dict__, namespace="/bots")
            
        except Exception as error:
            return ResponseFailure(data=str(error))

        else:
            return ResponseSuccess()





