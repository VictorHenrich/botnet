from server import Server
from server.http import (
    Controller,
    AbstractResponse,
    ResponseSuccess,
    ResponseInauthorized,
)
from middlewares import ValidationRequestBodyMiddleware, AuthenticationMiddleware
from models import User
from services.user.create_user import CreateUserService
from services.user.update_user import UpdateUserService
from services.user.delete_user import DeleteUserService
from services.user.auth_user import AuthUserService
from utils.entities import AuthUserBase, RegisterUserBase
from utils.constants import __ALGORITHMS_JWT__, __PAYLOAD_JWT__
from utils.patterns import IService
from utils.exceptions import UserNotFoundError, InvalidUserPasswordError


@Server.http.routes.view("/user/register")
class UserController(Controller):
    @ValidationRequestBodyMiddleware.apply(RegisterUserBase)
    async def post(self, body_request: RegisterUserBase) -> AbstractResponse:
        create_user_service: IService[None] = CreateUserService(
            body_request.email, body_request.password
        )

        create_user_service.execute()

        return ResponseSuccess()

    @ValidationRequestBodyMiddleware.apply(RegisterUserBase)
    @AuthenticationMiddleware.apply()
    async def put(self, auth: User, body_request: RegisterUserBase) -> AbstractResponse:
        update_user_service: IService[None] = UpdateUserService(
            auth, body_request.email, body_request.password
        )

        update_user_service.execute()

        return ResponseSuccess()

    @AuthenticationMiddleware.apply()
    async def delete(self, auth: User) -> AbstractResponse:
        delete_user_service: IService[None] = DeleteUserService(auth)

        delete_user_service.execute()

        return ResponseSuccess()


@Server.http.routes.view("/user/auth")
class UserAuthController(Controller):
    @ValidationRequestBodyMiddleware.apply(AuthUserBase)
    async def post(self, body_request: AuthUserBase) -> AbstractResponse:
        try:
            auth_user_service: IService[str] = AuthUserService(
                body_request.email, body_request.password
            )

            token: str = auth_user_service.execute()

            return ResponseSuccess(data=token)

        except UserNotFoundError or InvalidUserPasswordError as error:
            return ResponseInauthorized(str(error))
