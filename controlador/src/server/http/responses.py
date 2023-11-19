from typing import Any, Mapping, Optional
from aiohttp.web import Response
from abc import ABC
import json


class AbstractResponse(Response, ABC):
    __header_default: Mapping[str, str] = {"Content-Type": "application/json"}

    def __init__(
        self,
        data: Optional[Any],
        message_default: str,
        status_code: int,
        headers: Optional[Mapping[str, str]] = None,
    ) -> None:
        response_data: Mapping[str, Any] = {
            "status": status_code,
            "message": message_default,
        }

        response_headers: Mapping[str, str] = {
            **self.__class__.__header_default,
            **(headers or {}),
        }

        if data is not None:
            response_data["result"] = data

        super().__init__(
            body=json.dumps(response_data), headers=response_headers, status=status_code
        )


class ResponseSuccess(AbstractResponse):
    def __init__(
        self, data: Optional[Any] = None, headers: Optional[Mapping[str, str]] = None
    ) -> None:
        message_default: str = "OK"
        status_code: int = 200

        super().__init__(data, message_default, status_code, headers)


class ResponseFailure(AbstractResponse):
    def __init__(
        self, data: Optional[Any] = None, headers: Optional[Mapping[str, str]] = None
    ) -> None:
        message_default: str = "ERRO"
        status_code: int = 500

        super().__init__(data, message_default, status_code, headers)


class ResponseNotFound(AbstractResponse):
    def __init__(
        self, data: Optional[Any] = None, headers: Optional[Mapping[str, str]] = None
    ) -> None:
        message_default: str = "ROTA NÃO LOCALIZADA"
        status_code: int = 404

        super().__init__(data, message_default, status_code, headers)


class ResponseInauthorized(AbstractResponse):
    def __init__(
        self, data: Optional[Any] = None, headers: Optional[Mapping[str, str]] = None
    ) -> None:
        message_default: str = "NÃO AUTORIZADO"
        status_code: int = 401

        super().__init__(data, message_default, status_code, headers)
