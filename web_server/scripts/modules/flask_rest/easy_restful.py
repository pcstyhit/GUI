from datetime import datetime
from flask import make_response, send_from_directory
from flask_restful import Resource, Api, request


class HttpProxy(Resource):
    def writeTime(self, parm):
        ip = request.remote_addr
        nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')

        res = make_response(
            {"data": 'NONE', "state": True})
        res.status_code = 200
        with open('./request.txt', 'a+') as f:
            f.write(str(ip) + " >>> " + str(nowTime) +
                    ">>> request : \"GET\" /" + str(parm) + "\n")
        return res

    def get(self, parm):
        rea = self.writeTime(parm)
        return rea

    def post(self, parm):
        rea = self.writeTime(parm)
        return rea


class UploadFile(Resource):
    def get(self):
        return send_from_directory('./', 'request.txt', as_attachment=True)


def apiHandle(api: Api):
    api.add_resource(HttpProxy, '/<parm>')
    api.add_resource(UploadFile, '/download')
