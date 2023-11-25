from sqlalchemy import create_engine
from sqlalchemy.engine import create_engine, Engine
from sqlalchemy.orm.session import Session, sessionmaker
from sqlalchemy.orm.decl_api import declarative_base, DeclarativeMeta
from typing import Any, Type


class Database:
    def __init__(self, url: str, debug: bool = False) -> None:
        self.__engine: Engine = create_engine(url, echo=debug)

        self.__Model: Type[DeclarativeMeta] = declarative_base()

    @property
    def engine(self) -> Engine:
        return self.__engine

    @property
    def Model(self) -> Type[DeclarativeMeta]:
        return self.__Model

    def create_session(self, **options: Any) -> Session:
        return sessionmaker(bind=self.__engine, class_=Session, **options)()

    def migrate(self, drop_tables: bool = False) -> None:
        if drop_tables:
            self.__Model.metadata.drop_all(self.__engine)

        self.__Model.metadata.create_all(self.__engine)
