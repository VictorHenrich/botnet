from selenium.webdriver import Edge
from pathlib import Path

from services import server_client
from services.managers.manager_target import ManagerTarget



class RunBrowser(ManagerTarget):
    name: str = "rodar_navegador"
    debug: bool = False

    __executable_browser: str = str(Path().cwd() / 'targets' / 'web' / 'drives' / 'msedgedriver.exe')

    def execute(self):
        with Edge(RunBrowser.__executable_browser) as navegador:
            navegador.get('https://www.youtube.com/watch?v=xT1gflziHaQ')


server_client.manager_main.get_manager('automacao_navegador').append_targets(RunBrowser)