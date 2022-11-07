from services.utils.env import Env


data_env: dict = Env.get_values()


__HTTP__ = {
    "host": data_env['API_HOST'],
    "port": data_env['API_PORT'],
    "debug": False,
    "secret_key": data_env['API_SECRET_KEY']
}


__DATABASE__ = {
    "host": data_env['DB_HOST'],
    "port": data_env['DB_PORT'],
    "dbname": data_env['DB_NAME'],
    "username": data_env['DB_USER'],
    "password": data_env['DB_PASSWORD'],
    "dialect": data_env['DB_DIALECT'],
    "driver": data_env['DB_DRIVER'],
    "debug": False,
}