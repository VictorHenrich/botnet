import os
import sys

from start import client
from services.managers import ManagerTarget






class GetInfoUser(ManagerTarget):
    name: str = "abrir_bloco_notas"
    debug: bool = False


    def execute(self, data) -> None:
        nome_usuario: str = os.getlogin()

        sistema_operacional: str = sys.platform



client.managers.get_manager('automacao_so').append_targets(ManagerTarget)