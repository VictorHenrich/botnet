from typing import Optional
from dataclasses import dataclass
from sqlalchemy.orm.session import Session
from jwt import PyJWT
from datetime import datetime, timedelta

from server import Server
from repository.user.find_user_by_email import (
    FindUserByEmailRepository,
    IFindUserByEmailRepository,
)
from models import User
from utils.patterns import IFindRepository
from utils.exceptions import UserNotFoundError, InvalidUserPasswordError
from utils.crypt import CryptUtils
from utils.constants import __ALGORITHMS_JWT__, __PAYLOAD_JWT__
from utils.types import DictType


@dataclass
class FindUserByEmailProps:
    email: str


class AuthUserService:
    def __init__(self, email: str, password: str) -> None:
        self.__email: str = email

        self.__password: str = password

    def __find_user(self, session: Session) -> User:
        find_user_by_email_props: FindUserByEmailProps = FindUserByEmailProps(
            self.__email
        )

        find_repository: IFindRepository[
            IFindUserByEmailRepository, Optional[User]
        ] = FindUserByEmailRepository(session)

        user: User = find_repository.find(find_user_by_email_props)

        if not user:
            raise UserNotFoundError()

        return user

    def __generate_token(self, user: User) -> str:
        jwt_payload: DictType = {**__PAYLOAD_JWT__}

        jwt_payload["user"] = user.id_uuid

        jwt_payload["expired"] = (datetime.now() + timedelta(minutes=10)).timestamp()

        token: str = PyJWT().encode(
            jwt_payload,
            Server.http.configs["secret_key"],
            list(__ALGORITHMS_JWT__)[0],
        )

        return token

    def __auth_user(self) -> str:
        with Server.database.create_session() as session:
            user: User = self.__find_user(session)

            if not CryptUtils.compare_password(self.__password, user.password):
                raise InvalidUserPasswordError()

            return self.__generate_token(user)

    def execute(self) -> str:
        return self.__auth_user()
