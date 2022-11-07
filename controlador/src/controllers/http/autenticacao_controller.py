from typing import Any, Mapping
from jwt import PyJWT
from datetime import datetime, timedelta

from start import server
from services.http import (
    Controller,
    Response,
    ResponseSuccess,
    ResponseFailure
)
from middlewares import ValidacaoCorpoRequisicaoMiddleware
from models import Usuarios
from .bases import Usuario as BaseUsuario
from utils.constantes import (
    __ALGORITHMS_JWT__,
    __PAYLOAD_JWT__
)


@server.http.routes.view('/logar')
class AutenticacaoController(Controller):

    @ValidacaoCorpoRequisicaoMiddleware.apply(BaseUsuario)
    async def post(self, body_request: BaseUsuario) -> Response:
        try:
            with server.database.create_session() as session:
                usuario_localizado: Usuarios = \
                    session\
                        .query(Usuarios)\
                        .filter(
                            Usuarios.email == body_request.email,
                            Usuarios.senha == body_request.senha
                        )\
                        .first()

                if not usuario_localizado:
                    raise Exception('Usuário não localizado!')

                dados_jwt: Mapping[str, Any] = {**__PAYLOAD_JWT__}

                dados_jwt['user'] = usuario_localizado.id_uuid
                dados_jwt['expired'] = (datetime.now() + timedelta(minutes=10)).timestamp()

                token: str = \
                    PyJWT()\
                        .encode(
                            dados_jwt, 
                            server.http.configs['secret_key'], 
                            list(__ALGORITHMS_JWT__)[0]
                        )

        except Exception as error:
            return ResponseFailure(data=str(error))

        else:
            return ResponseSuccess(data=token)