from typing import Awaitable

from server import Server
from server.http import Controller, ResponseSuccess, AbstractResponse
from middlewares import AuthenticationMiddleware, ValidationRequestBodyMiddleware
from models import User
from utils.entities import ControlBase
from utils.patterns import IService
from services.bot.control_bots import ControlBotsService


@Server.http.routes.view("/bots/controle")
class BotController(Controller):
    @AuthenticationMiddleware.apply()
    @ValidationRequestBodyMiddleware.apply(ControlBase)
    async def post(self, auth: User, body_request: ControlBase) -> AbstractResponse:
        control_bots_service: IService[Awaitable[None]] = ControlBotsService(
            body_request.__dict__
        )

        await control_bots_service.execute()

        return ResponseSuccess()
