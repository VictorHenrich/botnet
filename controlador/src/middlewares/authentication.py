from aiohttp.web import Request
from server.http import AbstractResponse, ResponseInauthorized

from server.http import Middleware
from models import User
from utils.types import DictType
from utils.patterns import IService
from services.user.check_user_token import CheckUserTokenService


class AuthenticationMiddleware(Middleware):
    @classmethod
    async def call(cls, request: Request) -> DictType:
        headers: DictType = dict(request.headers)

        token: str = headers.get("Authorization", "")

        if not token:
            raise Exception("Campo de autenticação não localizado no cabecalho!")

        check_token_service: IService[User] = CheckUserTokenService(token)

        user: User = check_token_service.execute()

        return {"auth": user}

    @classmethod
    async def catch(cls, request: Request, exception: Exception) -> AbstractResponse:
        return ResponseInauthorized(data=str(exception))
