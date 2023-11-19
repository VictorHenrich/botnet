from client.utils import UtilEnv


data_env: dict = UtilEnv.get_values()


__SOCKET__ = {
    "url": data_env["URL_CONNECTION_SERVER"],
    "namespaces": UtilEnv.locate_keys(data_env, "NAMESPACE"),
}

__MANAGERS__ = UtilEnv.locate_keys(data_env, "MANAGER")
