from dataclasses import dataclass
from typing import Any, Mapping
from selenium.webdriver import Edge
from pathlib import Path

from services import client
from services.managers.manager_target import ManagerTarget



@dataclass
class AutomacaoNavegador:
    link: str

class RunBrowser(ManagerTarget):
    name: str = "rodar_navegador"
    debug: bool = False

    __executable_browser: str = str(Path().cwd() / 'targets' / 'web' / 'drives' / 'msedgedriver.exe')

    def execute(self, data: Mapping[str, Any]):
        dados_automacao: AutomacaoNavegador = AutomacaoNavegador(**data)

        with Edge(RunBrowser.__executable_browser) as navegador:
            navegador.get(dados_automacao.link)



client.manager_main.get_manager('automacao_navegador').append_targets(RunBrowser)