# s_http_server
simple restful api http server library

# Usage

```py
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
```

just extend Runserver class, and overwrite do method(do method return response class)

## Usage Response class

class response method with response, status_code paramters
```py
response_class = Response(response, status_code=201)
```
response parameter type is dict or str, dict type is convert to json

set_headers method has headers parameter

headers parameter is dict type

```py
headers = dict()
headers['Set-Cookie'] = 'test=test;'
headers['Server'] = 'Nginx;'
response_class.set_headers(headers)
```
