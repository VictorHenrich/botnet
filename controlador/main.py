from services import server
from aiohttp.web import Request


@server.http.routes.post('/controlar')
async def run(request: Request):

    data = await request.json()
    server.websocket.socket.emit('on_controller', data)


@server.start
def run_api():
    server.http.start()


server.start_server()





