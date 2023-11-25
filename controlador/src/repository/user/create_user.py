from typing import Protocol

from utils.patterns import AbstractRepository
from models import User


class ICreateUserRepository(Protocol):
    email: str
    password: str


class CreateUserRepository(AbstractRepository):
    def create(self, props: ICreateUserRepository) -> None:
        user: User = User(email=props.email.upper(), password=props.password)

        self.session.add(user)
