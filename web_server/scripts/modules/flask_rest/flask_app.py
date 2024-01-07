from flask import Flask, render_template
from flask_restful import Api
from flask_socketio import SocketIO
from flask_cors import CORS

from scripts.libs import CONFIGS
from .easy_restful import apiHandle
from .websocket import webSocketHandle

app = Flask(__name__)


def init_app():
    # 设置静态文件的路径
    template_folder = f"{CONFIGS['project_path']}/{CONFIGS['example']}"
    static_url_path = ""
    static_folder = f"{CONFIGS['project_path']}/{CONFIGS['example_dependencies_path']}"

    app = Flask(__name__,
                template_folder=template_folder,
                static_url_path=static_url_path,
                static_folder=static_folder)
    # 允许跨域
    CORS(app, supports_credentials=True)

    # 声明restful api
    api = Api(app)
    apiHandle(api)

    # 挂载静态网页的路由
    @app.route('/')
    def index():
        return render_template('index.html')


def run_default_app():
    init_app()
    app.run(host="0.0.0.0", port=5000)


def run_socket_app():
    init_app()
    # 创建为websocket服务
    socketio = SocketIO(app, cors_allowed_origins='*')
    webSocketHandle(socketio)
    socketio.run(app, host='0.0.0.0', port=5000)


def run_defaut_ssl_app():
    init_app()
    app.run(host="0.0.0.0", port=5000, ssl_context=(
        './cert/server.crt', './cert/server.key'))


def run_socket_ssl_app():
    pass
