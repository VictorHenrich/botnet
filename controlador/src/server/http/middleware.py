from abc import ABC, abstractclassmethod
from typing import Any, Coroutine, Mapping, Optional, Sequence
from aiohttp.web import Request, Response


class Middleware(ABC):
    @abstractclassmethod
    async def call(
        cls, request: Request, *args: Sequence[Any], **kwargs: Mapping[str, Any]
    ) -> Optional[Mapping[str, Any]]:
        pass

    @abstractclassmethod
    async def catch(cls, request: Request, exception: Exception) -> Response:
        raise exception

    @classmethod
    def apply(cls, *args: Sequence[Any], **kwargs: Mapping[str, Any]) -> Coroutine:
        def wrapper(function: Coroutine) -> Coroutine:
            async def w(*a: Sequence[Any], **k: Mapping[str, Any]) -> Response:
                try:
                    object_request: Request = a[0].request

                    result: Optional[Mapping[str, Any]] = await cls.call(
                        object_request, *args
                    )

                except Exception as error:
                    return await cls.catch(object_request, error)

                else:
                    return await function(*a, **{**k, **(result or {})})

            return w

        return wrapper
