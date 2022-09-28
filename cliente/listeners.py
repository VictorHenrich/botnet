from services import server_client


@server_client.websocket.socket.on('on_controller')
def rodar_nevegador(dados):
    server_client.manager_main.execute('automacao_navegador', 'rodar_navegador')