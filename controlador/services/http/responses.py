from typing import Any, Mapping, Optional
from aiohttp.web import Response
import json


header_default: Mapping[str, str] = {
    "Content-Type": "application/json"
}



class ResponseSuccess(Response):
    def __init__(
        self,
        status_code: int = 200,
        data: Optional[Any] = None,
        headers: Mapping[str, str] = header_default
    ) -> None:
        response_data: Mapping[str, Any] = {
            "status": status_code,
            "message": "OK"
        }

        if data is not None:
            response_data['result'] = data

        super().__init__(
            body=json.dumps(response_data),
            status=status_code,
            headers={**header_default, **headers}
        )


class ResponseFailure(Response):
    def __init__(
        self,
        status_code: int = 500,
        data: Optional[Any] = None,
        headers: Mapping[str, str] = header_default
    ) -> None:
        response_data: Mapping[str, Any] = {
            "status": status_code,
            "message": "ERRO"
        }

        if data is not None:
            response_data['result'] = data

        super().__init__(
            body=json.dumps(response_data),
            status=status_code,
            headers={**header_default, **headers}
        )


class ResponseNotFound(Response):
    def __init__(
        self,
        status_code: int = 404,
        data: Optional[Any] = None,
        headers: Mapping[str, str] = header_default
    ) -> None:
        response_data: Mapping[str, Any] = {
            "status": status_code,
            "message": "ROTA NÃO LOCALIZADA"
        }

        if data is not None:
            response_data['result'] = data

        super().__init__(
            body=json.dumps(response_data),
            status=status_code,
            headers={**header_default, **headers}
        )