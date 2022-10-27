from aiohttp.web import Request
from typing import Any, Mapping
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
        try:
            headers: Mapping[str, str] = dict(request.headers)

            token: str = headers['Authorization']

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


        except KeyError:
            raise Exception('Campo de autenticação não localizado no cabecalho!')


