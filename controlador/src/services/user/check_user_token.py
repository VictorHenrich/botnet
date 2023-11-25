from typing import Optional
from dataclasses import dataclass
from sqlalchemy.orm.session import Session
from jwt import PyJWT
from datetime import datetime

from server import Server
from repository.user.find_user_by_uuid import (
    FindUserByUUIDRepository,
    IFindUserByUUIDRepository,
)
from models import User
from utils.patterns import IFindRepository
from utils.exceptions import ExpiredTokenError, UserNotFoundError
from utils.types import DictType
from utils.constants import __ALGORITHMS_JWT__, __PAYLOAD_JWT__


@dataclass
class FindUserByEmailProps:
    user_uuid: str


class CheckUserTokenService:
    def __init__(self, token: str) -> None:
        self.__token: str = token

    def __get_auth_payload_in_token(self) -> DictType:
        auth_payload: DictType = {
            prop: value
            for prop, value in PyJWT()
            .decode(
                self.__token,
                Server.http.configs["secret_key"],
                list(__ALGORITHMS_JWT__),
            )
            .items()
            if prop in __PAYLOAD_JWT__.keys()
        }

        if auth_payload["expired"] <= datetime.now().timestamp():
            raise ExpiredTokenError()

        return auth_payload

    def __find_user(self, session: Session, user_uuid: str) -> User:
        find_user_by_email_props: FindUserByEmailProps = FindUserByEmailProps(user_uuid)

        find_repository: IFindRepository[
            IFindUserByUUIDRepository, Optional[User]
        ] = FindUserByUUIDRepository(session)

        user: User = find_repository.find(find_user_by_email_props)

        if not user:
            raise UserNotFoundError()

        return user

    def __verify_token(self) -> User:
        auth_payload: DictType = self.__get_auth_payload_in_token()

        with Server.database.create_session() as session:
            return self.__find_user(session, auth_payload["user"])

    def execute(self) -> User:
        return self.__verify_token()
