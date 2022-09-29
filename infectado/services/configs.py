from services.managers.manager import Manager


__URL_SOCKET__: str = "ws://localhost:6000"

__MANAGERS__: list[Manager] = [
    Manager('automacao_navegador'),
    Manager('automacao_so')
]