from abc import ABC, abstractmethod
from typing import Any, Awaitable, Mapping, Optional, Callable
from aiohttp.web import Request

from .responses import AbstractResponse


class Middleware(ABC):
    @classmethod
    @abstractmethod
    async def call(
        cls, request: Request, *args: Any, **kwargs: Any
    ) -> Optional[Mapping[str, Any]]:
        pass

    @classmethod
    @abstractmethod
    async def catch(cls, request: Request, exception: Exception) -> AbstractResponse:
        raise exception

    @classmethod
    def apply(cls, *args: Any, **kwargs: Any) -> Callable[[Any], Callable]:
        def decorator(
            function: Callable[[Any], Awaitable]
        ) -> Callable[[Any], Awaitable]:
            async def wrapper(*a: Any, **k: Any) -> AbstractResponse:
                try:
                    object_request: Request = a[0].request

                    result: Optional[Mapping[str, Any]] = await cls.call(
                        object_request, *args, **kwargs
                    )

                except Exception as error:
                    return await cls.catch(object_request, error)

                else:
                    return await function(*a, **{**k, **(result or {})})

            return wrapper

        return decorator
