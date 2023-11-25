class UserNotFoundError(Exception):
    def __init__(self) -> None:
        super().__init__("Usuário não localizado!")


class InvalidUserPasswordError(Exception):
    def __init__(self) -> None:
        super().__init__("Senha do usuário passada é inválida a cadastrada!")


class ExpiredTokenError(Exception):
    def __init__(self) -> None:
        super().__init__("Token do usuário expirado!")
