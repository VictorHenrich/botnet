from typing import Protocol

from utils.patterns import AbstractRepository
from models import User


class IUpdateUserRepository(Protocol):
    email: str
    password: str
    user: User


class UpdateUserRepository(AbstractRepository):
    def update(self, props: IUpdateUserRepository) -> None:
        props.user.email = props.email.upper()

        props.user.password = props.password

        self.session.add(props.user)
