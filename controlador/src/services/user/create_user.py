from dataclasses import dataclass

from server import Server
from repository.user.create_user import CreateUserRepository, ICreateUserRepository
from utils.patterns import ICreateRepository
from utils.crypt import CryptUtils


@dataclass
class CreateUserProps:
    email: str
    password: str


class CreateUserService:
    def __init__(self, email: str, password: str) -> None:
        self.__email: str = email

        self.__password: str = password

    def __create_user(self) -> None:
        password_encrypted: str = CryptUtils.encrypt_password(self.__password)

        create_user_props: CreateUserProps = CreateUserProps(
            self.__email, password_encrypted
        )

        with Server.database.create_session() as session:
            create_repository: ICreateRepository[
                ICreateUserRepository, None
            ] = CreateUserRepository(session)

            create_repository.create(create_user_props)

            session.commit()

    def execute(self) -> None:
        self.__create_user()
