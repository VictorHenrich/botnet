from typing import Any, Mapping
from jwt import PyJWT
from datetime import datetime, timedelta
import bcrypt

from start import server
from server.http import (
    Controller,
    Response,
    ResponseSuccess,
    ResponseInauthorized,
)
from middlewares import ValidacaoCorpoRequisicaoMiddleware, AutenticacaoMiddlware
from models import Usuarios
from .bases import AutenticacaoUsuario, CadastroUsuario
from utils.constantes import __ALGORITHMS_JWT__, __PAYLOAD_JWT__


@server.http.routes.view("/usuario")
class UsuarioController(Controller):
    @ValidacaoCorpoRequisicaoMiddleware.apply(CadastroUsuario)
    async def post(self, body_request: CadastroUsuario) -> Response:
        with server.database.create_session() as session:
            senha_criptograda: str = str(
                bcrypt.hashpw(body_request.senha.encode("utf-8"), bcrypt.gensalt())
            )

            usuario: Usuarios = Usuarios(
                email=body_request.email.lower(), senha=senha_criptograda
            )

            session.add(usuario)

            session.commit()

        return ResponseSuccess()

    @AutenticacaoMiddlware.apply()
    @ValidacaoCorpoRequisicaoMiddleware.apply(CadastroUsuario)
    async def put(self, auth: Usuarios, body_request: CadastroUsuario) -> Response:
        with server.database.create_session() as session:
            senha_criptograda: str = str(
                bcrypt.hashpw(body_request.senha.encode("utf-8"), bcrypt.gensalt())
            )

            auth.email = body_request.email.lower()

            auth.senha = senha_criptograda

            session.add(auth)

            session.commit()

        return ResponseSuccess()

    @AutenticacaoMiddlware.apply()
    async def delete(self, auth: Usuarios) -> Response:
        with server.database.create_session() as session:
            session.delete(auth)

            session.commit()

        return ResponseSuccess()


@server.http.routes.view("/usuario/autenticacao")
class AutenticacaoController(Controller):
    @ValidacaoCorpoRequisicaoMiddleware.apply(AutenticacaoUsuario)
    async def post(self, body_request: AutenticacaoUsuario) -> Response:
        with server.database.create_session() as session:
            usuario_localizado: Usuarios = (
                session.query(Usuarios)
                .filter(Usuarios.email == body_request.email)
                .first()
            )

            if not usuario_localizado:
                return ResponseInauthorized(
                    data="Nenhum usuário foi localizado através do email passado!"
                )

            if not bcrypt.checkpw(
                body_request.senha.encode("utf-8"),
                usuario_localizado.senha.encode("utf-8"),
            ):
                return ResponseInauthorized(data="Senha passada é incorreta!")

            dados_jwt: Mapping[str, Any] = {**__PAYLOAD_JWT__}

            dados_jwt["user"] = usuario_localizado.id_uuid

            dados_jwt["expired"] = (datetime.now() + timedelta(minutes=10)).timestamp()

            token: str = PyJWT().encode(
                dados_jwt,
                server.http.configs["secret_key"],
                list(__ALGORITHMS_JWT__)[0],
            )

        return ResponseSuccess(data=token)
