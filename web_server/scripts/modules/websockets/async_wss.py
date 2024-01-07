import asyncio
import websockets
import json
import ssl

from scripts.libs import CONFIGS


_URL = '0.0.0.0'
_PORT = CONFIGS['default_ws_port']
SSL_CONTEXT = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)


def initSSL():
    certfile = f"{CONFIGS['cert_path']}/server.crt"
    keyfile = f"{CONFIGS['cert_path']}/server.key"
    SSL_CONTEXT.load_cert_chain(
        certfile=certfile, keyfile=keyfile)
    SSL_CONTEXT.check_hostname = False
    SSL_CONTEXT.verify_mode = ssl.CERT_NONE


async def connectWSS(websocket):
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


async def wssHandle(websocket, path):
    await asyncio.wait([
        asyncio.create_task(connectWSS(websocket)),
        asyncio.create_task(sendMsg(websocket))
    ])


def asyncWSS(loop:asyncio.BaseEventLoop):
    initSSL()
    asyncio.set_event_loop(loop)
    wsServer = websockets.serve(
        wssHandle, _URL, _PORT, ping_interval=None, ssl=SSL_CONTEXT)
    loop.run_until_complete(wsServer)
    print("Wss server Run on  ... IP: {}, Port {}".format(_URL, _PORT))
    loop.run_forever()
