# from flask import Flask, render_template
# from flask_restful import Api
# from flask_socketio import SocketIO
# from flask_cors import CORS

# from modules.restful import apiHandle
# from modules.ws import webSocketHandle
# from modules.async_ws import asyncWS
# from modules.async_wss import asyncWSS

# import threading
# import asyncio

# # 设置静态文件的路径
# app = Flask(__name__, template_folder="./",
#             static_url_path="", static_folder="./")

# # 允许跨域
# CORS(app, supports_credentials=True)

# # 声明restful api
# api = Api(app)
# apiHandle(api)

# # 创建为websocket服务
# # socketio = SocketIO(app, cors_allowed_origins='*')
# # webSocketHandle(socketio)



# # 挂载静态网页的路由
# @app.route('/')
# def index():
#     return render_template('index.html')


# loop = asyncio.new_event_loop()
# ttws = threading.Thread(target=asyncWSS, args=(loop,))
# ttws.start()

# # 启动服务
# # app.run(host="0.0.0.0", port=5000, ssl_context=('./cert/server.crt','./cert/server.key'))

# # 采用websocket的启动方式



# # socketio.run(app, host='0.0.0.0', port=5000)
# ttws.join()

import os

if __name__ == '__main__':
    from scripts.modules.flask_rest import flask_app
    
    
