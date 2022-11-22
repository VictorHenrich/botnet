from typing import Mapping, Type, Any
from aiohttp.web import Request
from server.http import Middleware
from pydantic import BaseModel, ValidationError




class ValidacaoCorpoRequisicaoMiddleware(Middleware):
    @classmethod
    async def call(cls, request: Request, class_body: Type[BaseModel]) -> Mapping[str, Any]:
        json_corpo_requisicao: Mapping[str, Any] = await request.json()

        try:
            objeto_corpo_requisicao: Any = class_body(**json_corpo_requisicao)

        except ValidationError:
            raise Exception('Corpo da requisição é inválido!')

        else:
            return {'body_request': objeto_corpo_requisicao}

