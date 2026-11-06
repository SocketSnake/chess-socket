import socket

class Server:
    def __init__(self, ip_addr: str, port: int):
        self.ip_addr = ip_addr
        self.port = port

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip_addr, port))
        
        self.server_socket.listen(5)


    def send_data(self):
        pass