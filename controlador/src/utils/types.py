from typing import Mapping, Any, TypeAlias
from aiohttp.web import Request


DictType: TypeAlias = Mapping[str, Any]


RequestType: TypeAlias = Request
