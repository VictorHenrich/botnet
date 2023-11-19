from typing import Any, Callable, Coroutine, Mapping, Sequence
import asyncio


class UtilAsync:
    @classmethod
    def run(cls, function: Callable[[Any], Coroutine]):
        def wrapper(*args: Sequence[Any], **kwargs: Mapping[str, Any]):
            return asyncio.run(function(*args, **kwargs))

        return wrapper
