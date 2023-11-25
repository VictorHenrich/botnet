from server import Server


@Server.start
def migrate_database():
    import models

    Server.database.migrate()


@Server.start
def run_api():
    import controllers

    Server.http.start()


Server.start_app()
