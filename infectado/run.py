from services import server_client


@server_client.start
def load_targets():
    import targets
    import listeners

    server_client.websocket.start()


server_client.start_server()
