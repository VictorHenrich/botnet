from typing import Protocol, Optional

from utils.patterns import AbstractRepository
from models import User


class IFindUserByEmailRepository(Protocol):
    email: str


class FindUserByEmailRepository(AbstractRepository):
    def find(self, props: IFindUserByEmailRepository) -> Optional[User]:
        return (
            self.session.query(User).filter(User.email == props.email.upper()).first()
        )
