from abc import ABC
from typing import Optional, Protocol, Generic, TypeVar, Union, Sequence
from sqlalchemy.orm.session import Session


T = TypeVar("T", covariant=True)

P = TypeVar("P", contravariant=True)

M = TypeVar("M", covariant=True)


class IService(Protocol, Generic[T]):
    def execute(self) -> T:
        ...


class AbstractRepository(ABC):
    def __init__(self, session: Session) -> None:
        self.__session: Session = session

    @property
    def session(self) -> Session:
        return self.__session


class IFindRepository(Protocol, Generic[P, M]):
    def find(self, props: P) -> Union[Optional[M], Sequence[M]]:
        ...


class IUpdateRepository(Protocol, Generic[P, M]):
    def update(self, props: P) -> M:
        ...


class ICreateRepository(Protocol, Generic[P, M]):
    def create(self, props: P) -> M:
        ...


class IDeleteRepository(Protocol, Generic[P, M]):
    def delete(self, props: P) -> M:
        ...
