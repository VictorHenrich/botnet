from typing import Any, Mapping, Optional
from pydantic import BaseModel, validator



class Controle(BaseModel):
    module: str
    targets: list[str]
    args: Optional[Mapping[str, Any]] = None


    @validator('targets', pre=True)
    def tratar_alvos(cls, value: list[str]):
        return list(set(value))