from pathlib import Path
from dotenv import dotenv_values
from typing import Mapping, Union, Optional, Sequence


class Env:
    __path_default: Sequence[Path] = list(Path.cwd().glob("*.env"))

    @classmethod
    def get_values(
        cls, path: Optional[Union[Path, str]] = None
    ) -> Mapping[str, Optional[str]]:
        path_: Path = Path(path or cls.__path_default[0])

        if not path_.exists():
            raise Exception("Não foi possível localizar arquivo .env!")

        return dotenv_values(str(path_))
