from services.utils.env import Env


data_env: dict = Env.get_values()


__HOST__: str = data_env['API_HOST']

__PORT__: int = data_env['API_PORT']

__DEBUG__: bool = False

__SECRET_KEY__: str = data_env['API_SECRET_KEY']

__URL_BASE__: str = f"postgresql+psycopg2://{data_env['DB_USER']}:{data_env['DB_PASSWORD']}@{data_env['DB_HOST']}:{data_env['DB_PORT']}/{data_env['DB_NAME']}"

