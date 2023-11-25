from dataclasses import dataclass

from server import Server
from repository.user.update_user import UpdateUserRepository, IUpdateUserRepository
from utils.patterns import IUpdateRepository
from utils.crypt import CryptUtils
from models import User


@dataclass
class UpdateUserProps:
    user: User
    email: str
    password: str


class UpdateUserService:
    def __init__(self, user: User, email: str, password: str) -> None:
        self.__user: User = user

        self.__email: str = email

        self.__password: str = password

    def __update_user(self) -> None:
        password_encrypted: str = CryptUtils.encrypt_password(self.__password)

        update_user_props: UpdateUserProps = UpdateUserProps(
            self.__user, self.__email, password_encrypted
        )

        with Server.database.create_session() as session:
            update_repository: IUpdateRepository[
                IUpdateUserRepository, None
            ] = UpdateUserRepository(session)

            update_repository.update(update_user_props)

            session.commit()

    def execute(self) -> None:
        self.__update_user()
