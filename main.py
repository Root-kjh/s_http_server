from s_http_server.core.response import Response
from s_http_server.core.runserver import Runserver

class RestHttpServer(Runserver):
    def do(self, request):
        response = dict()
        response['test1'] = 'test1'
        response['test2'] = 'test2'
        return Response(response, status_code=201)


if __name__ == '__main__':
    server = RestHttpServer()
    server.runserver('127.0.0.1', 80)