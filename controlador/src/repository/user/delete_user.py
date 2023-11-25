from typing import Protocol

from utils.patterns import AbstractRepository
from models import User


class IDeleteUserRepository(Protocol):
    user: User


class DeleteUserRepository(AbstractRepository):
    def delete(self, props: IDeleteUserRepository) -> None:
        self.session.delete(props.user)
