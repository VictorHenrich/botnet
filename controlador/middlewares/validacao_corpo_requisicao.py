from typing import Mapping, Type, Any
from aiohttp.web import Request
from services.http import Middleware




class ValidacaoCorpoRequisicaoMiddleware(Middleware):
    @classmethod
    async def call(cls, request: Request, class_body: Type) -> Mapping[str, Any]:
        try:
            json_corpo_requisicao: Mapping[str, Any] = await request.json()


            objeto_corpo_requisicao: Any = class_body(**json_corpo_requisicao)

        except ValueError:
            raise Exception('Corpo da requisição é inválido!')

        else:
            return {'body_request': objeto_corpo_requisicao}

