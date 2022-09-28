from services import server_client
from services.managers.manager_target import ManagerTarget



class RodarNevegador(ManagerTarget):
    name: str = "rodar_navegador"
    debug: bool = False


    def execute(self):
        print('ta funcionandooooo')


server_client.manager_main.get_manager('automacao_navegador').append_targets(RodarNevegador)