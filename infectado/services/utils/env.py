from pathlib import Path
from dotenv import dotenv_values
from typing import Mapping, Union, Optional


class Env:
    __path_default, = Path.cwd().glob('*.env')

    @classmethod
    def get_values(cls, path: Optional[Union[Path, str]] = None) -> Mapping[str, Optional[str]]:
        path_: Path = Path(path or cls.__path_default)

        if not path_.exists():
            raise Exception('Não foi possível localizar arquivo .env!')

        return dotenv_values(str(path_))


    @classmethod
    def locate_keys(cls, data_env: Mapping[str, Optional[str]], name: str):
        return [
            value_env
            for key_env, value_env in data_env.items()
            if (key_env or '').upper().startswith(name.upper())
        ]
