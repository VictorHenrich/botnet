from aiohttp.web import Request
from typing import Any, Mapping
from services.http import Response, ResponseInauthorized
from jwt import PyJWT
from datetime import datetime

from services import server
from services.http import Middleware
from utils.constantes import (
    __ALGORITHMS_JWT__,
    __PAYLOAD_JWT__
)
from models import Usuarios



class AutenticacaoMiddlware(Middleware):
    @classmethod
    async def call(cls, request: Request) -> Mapping[str, Usuarios]:
        headers: Mapping[str, str] = dict(request.headers)

        token: str = headers.get('Authorization')

        if not token:
            raise Exception('Campo de autenticação não localizado no cabecalho!')

        dados_autenticacao: Mapping[str, Any] = \
            {
                prop: value
                for prop, value in PyJWT()\
                                        .decode(
                                            token, 
                                            server.http.configs['secret_key'], 
                                            list(__ALGORITHMS_JWT__)                                        
                                        )\
                                        .items()

                if prop in __PAYLOAD_JWT__.keys()
            }

        
        if dados_autenticacao['expired'] <= datetime.now().timestamp():
            raise Exception('Token expirado!')

        with server.database.create_session() as session:
            usuario_localizado: Usuarios = \
                session\
                    .query(Usuarios)\
                    .filter(Usuarios.id_uuid == dados_autenticacao['user'])

            if not usuario_localizado:
                raise Exception('Usuário não localizado!')

            return {
                'auth': usuario_localizado
            }


    @classmethod
    async def catch(cls, request: Request, exception: Exception) -> Response:
        return ResponseInauthorized(data=str(exception))


