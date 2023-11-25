from typing import Protocol, Optional

from utils.patterns import AbstractRepository
from models import User


class IFindUserByUUIDRepository(Protocol):
    user_uuid: str


class FindUserByUUIDRepository(AbstractRepository):
    def find(self, props: IFindUserByUUIDRepository) -> User:
        user: Optional[User] = (
            self.session.query(User).filter(User.id_uuid == props.user_uuid).first()
        )

        if not user:
            raise Exception("Usuário não localizado!")

        return user
