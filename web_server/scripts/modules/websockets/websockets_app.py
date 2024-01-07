import asyncio
import threading

from .async_ws import asyncWS
from .async_wss import asyncWSS

def run_async_ws():
    loop_ws = asyncio.new_event_loop()
    t_ws = threading.Thread(target=asyncWS, args=(loop_ws,))
    t_ws.start()
    t_ws.join()

def run_async_wss():
    loop_wss = asyncio.new_event_loop()
    t_wss = threading.Thread(target=asyncWSS, args=(loop_wss,))
    t_wss.start()
    t_wss.join()