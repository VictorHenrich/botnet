from services.utils.env import Env


data_env: dict = Env.get_values()


__URL_SOCKET__: str = data_env['URL_CONNECTION_SERVER']

__MANAGERS__: list[str] = [
    data_env['MANAGER_AUTOMATE_BROWSER'],
    data_env['MANAGER_AUTOMATE_SO']
]
