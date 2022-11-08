from start import client


@client.start
def load_targets():
    import targets
    import controllers

    client.websocket.start()


client.start_client()
