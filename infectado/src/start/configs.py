from services.utils.env import Env


data_env: dict = Env.get_values()


__SOCKET__ = {
    "url": data_env['URL_CONNECTION_SERVER'],
    "namespaces": Env.locate_keys(data_env, 'NAMESPACE')
}

__MANAGERS__ = Env.locate_keys(data_env, 'MANAGER')