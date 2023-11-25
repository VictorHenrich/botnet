from server import Server
from settings import __DATABASE__, __HTTP__


@Server.start
def migrate_database():
    import models

    Server.database.migrate()


@Server.start
def run_api():
    import controllers

    Server.http.start()


Server.init_app(__HTTP__, __DATABASE__)

Server.start_app()
