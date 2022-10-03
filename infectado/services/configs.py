from services.utils.env import Env


data_env: dict = Env.get_values()


__URL_SOCKET__: str = data_env['URL_CONNECTION_SERVER']

__MANAGERS__: list[str] = [
    value_env
    for key_env, value_env in data_env.items()
    if (key_env or '' ).upper().startswith('MANAGER')
]
