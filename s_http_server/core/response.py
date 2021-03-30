from http.client import responses
import json 

class Response():
    def __init__(self, response, status_code = 200):
        self.start_line = f'HTTP/1.1 {status_code} {responses[status_code]}'
        self.headers = dict()
        self.headers['Content-Type'] = "application/json"
        self.set_body(response)

    def set_headers(self, headers):
        self.headers.update(headers)
    
    def set_body(self, body):
        if type(body)==str:
            self.body = body            
        elif type(body)==dict:
            self.body = json.dumps(body)
        else:
            raise Exception("body type is not supported")
        self.headers['Content-Length'] = len(self.body)

    def __str__(self):
        header = '\n'.join([f'{key}: {value}' for key, value in self.headers.items()])
        return f'{self.start_line}\n{header}\n\n{self.body}'