from aiohttp.web import (
    Application, 
    RouteTableDef, 
    view,
    run_app
)
from typing import Mapping, Any, Union
from pathlib import Path

from .controller import Controller


class ServerHttp:
    def __init__(
        self,
        host: str,
        port: int,
        debug: bool = False
    ) -> None:
        self.__configs: Mapping[str, Any] = {
            "host": host,
            "port": port
        }

        self.__app: Application = Application(debug=debug)

        self.__routes: RouteTableDef = RouteTableDef()

    @property
    def configs(self) -> Mapping[str, Any]:
        return self.__configs

    @property
    def app(self) -> Application:
        return self.__app

    @property
    def routes(self) -> RouteTableDef:
        return self.__routes

    def start(self) -> None:
        run_app(self.__app, **self.__configs)

    def append_route(self, path: Union[Path, str], controller: Controller) -> None:
        view(str(path), controller)