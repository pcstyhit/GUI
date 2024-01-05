import asyncio
import websockets
import json


_URL = '0.0.0.0'
_PORT = 10000


async def connectWS(websocket):
    print('[INFO]- WebSocket Connect Success!')
    while True:
        try:
            recvMsg = await websocket.recv()
            print('[INFO]- Get message : ', recvMsg)
            if recvMsg == '':
                print("Client has closed.")
        except Exception as e:
            print("Client has closed. See ", e)
            break


async def sendMsg(websocket):
    while True:
        try:
            await websocket.send(json.dumps("Hello, I am python"))
        except Exception as e:
            print("Client has closed See {}".format(e))
            break
        await asyncio.sleep(1)


async def wsHandle(websocket, path):
    await asyncio.wait([
        asyncio.create_task(connectWS(websocket)),
        asyncio.create_task(sendMsg(websocket))
    ])


def asyncWS(loop):
    asyncio.set_event_loop(loop)
    wsServer = websockets.serve(wsHandle, _URL, _PORT, ping_interval=None)
    loop.run_until_complete(wsServer)
    print("Ws server Run on  ... IP: {}, Port {}".format(_URL, _PORT))
    loop.run_forever()
