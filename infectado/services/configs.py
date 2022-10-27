
from services.utils.env import Env


data_env: dict = Env.get_values()


__URL_SOCKET__: str = data_env['URL_CONNECTION_SERVER']

__NAMESPACES__: list[str] = Env.locate_keys(data_env, 'NAMESPACE')

__MANAGERS__: list[str] = Env.locate_keys(data_env, 'MANAGER')
