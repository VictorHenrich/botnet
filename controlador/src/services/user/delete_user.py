from dataclasses import dataclass

from server import Server
from repository.user.delete_user import IDeleteUserRepository, DeleteUserRepository
from utils.patterns import IDeleteRepository
from models import User


@dataclass
class DeleteUserProps:
    user: User


class DeleteUserService:
    def __init__(self, user: User) -> None:
        self.__user: User = user

    def __delete_user(self) -> None:
        delete_user_props: DeleteUserProps = DeleteUserProps(self.__user)

        with Server.database.create_session() as session:
            delete_repository: IDeleteRepository[
                IDeleteUserRepository, None
            ] = DeleteUserRepository(session)

            delete_repository.delete(delete_user_props)

            session.commit()

    def execute(self) -> None:
        self.__delete_user()
