from typing import Any, Mapping, Optional
from pydantic import BaseModel, validator


class ControlBase(BaseModel):
    module: str
    targets: list[str]
    args: Optional[Mapping[str, Any]] = None

    @validator("targets", pre=True)
    def tratar_alvos(cls, value: list[str]):
        return list(set(value))


class AuthUserBase(BaseModel):
    email: str
    password: str

    @validator("email")
    def validar_email(cls, value: str) -> str:
        if "@" not in value:
            raise Exception("Campo email necessita ser um email válido!")

        return value


class RegisterUserBase(BaseModel):
    email: str
    password: str

    @validator("email")
    def validar_email(cls, value: str) -> str:
        if "@" not in value:
            raise Exception("Campo email necessita ser um email válido!")

        return value
