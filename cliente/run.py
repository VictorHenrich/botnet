from services import server_client


@server_client.start
def carregar_alvos():
    import targets
    import listeners

    server_client.websocket.start()


server_client.start_server()
