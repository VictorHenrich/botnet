from socketio import AsyncServer
from aiohttp.web import Application, run_app, RouteTableDef, Response
from time import sleep

routes = RouteTableDef()

@routes.get('/fazer')
async def rodar(request):
    await sio.emit('on_controller', {'module': 'OK'})

    return Response(text="TUDO BEM")


app = Application()
sio = AsyncServer()

sio.attach(app)
app.add_routes(routes)


run_app(app, host='localhost', port=6000)




