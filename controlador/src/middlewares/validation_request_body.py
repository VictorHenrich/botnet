from typing import Type, Any
from aiohttp.web import Request
from server.http import Middleware
from pydantic import BaseModel, ValidationError

from utils.types import DictType


class ValidationRequestBodyMiddleware(Middleware):
    @classmethod
    async def call(cls, request: Request, class_body: Type[BaseModel]) -> DictType:
        json_payload: DictType = await request.json()

        try:
            body_request: Any = class_body(**json_payload)

        except ValidationError:
            raise Exception("Corpo da requisição é inválido!")

        else:
            return {"body_request": body_request}
