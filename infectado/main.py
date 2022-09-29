from services import client


@client.start
async def load_targets():
    import targets
    import listeners

    await client.websocket.start()


client.start_client()
