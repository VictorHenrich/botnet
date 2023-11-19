from pydantic import BaseModel, validator


class AutenticacaoUsuario(BaseModel):
    email: str
    senha: str

    @validator("email")
    def validar_email(cls, value: str) -> str:
        if "@" not in value:
            raise Exception("Campo email necessita ser um email válido!")

        return value


class CadastroUsuario(BaseModel):
    email: str
    senha: str

    @validator("email")
    def validar_email(cls, value: str) -> str:
        if "@" not in value:
            raise Exception("Campo email necessita ser um email válido!")

        return value
