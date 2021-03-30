from .request import Request
import socket

class Runserver():
    def do(self, request):
        pass

    def runserver(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((host, port))
            server_socket.listen()
            while True:
                try:
                    client_socket, addr = server_socket.accept()
                    data = client_socket.recv(1024)
                    request = Request(data.decode(), addr[0])
                    print(self.do(request))
                    print(str(self.do(request)).encode())
                    client_socket.send(str(self.do(request)).encode())
                    client_socket.close()
                except KeyboardInterrupt:
                    if client_socket:
                        client_socket.close()
                    if server_socket:
                        server_socket.close()
                    break
                    