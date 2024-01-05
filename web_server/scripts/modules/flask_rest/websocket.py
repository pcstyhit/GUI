from flask_socketio import SocketIO

# 作用域，需要和网页的websocket一致
space = '/dcenter'


def webSocketHandle(socketio: SocketIO):
    # 连接websocket
    @socketio.on('connect', namespace=space)
    def connect_handler():
        # 向网页发送websockt消息
        socketio.emit('message', "connect ok ", namespace=space)

    # 错误输出
    @socketio.on_error_default
    def default_error_handler(e):
        print("Error See: ", e)

    # 断开连接
    @socketio.on('disconnect')
    def disconnect_msg():
        print('Web socket disconnect.')
