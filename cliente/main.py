from services import client


@client.start
def load_targets():
    import targets
    import listeners

    client.websocket.start()


client.start_client()
