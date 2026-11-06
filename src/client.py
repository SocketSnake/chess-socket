import socket

class Client:
    def __init__(self, ip_addr: str, port: int):
        self.ip_addr = ip_addr
        self.port = port

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((ip_addr, port))


    def send_client_data():
        self.client_socket.sendall("Привет как дела сервер?".encode('utf-8'))

    def get_client_data(self):
        data = self.client_socket.recv(1024)
        print(f"Сообщение от сервера:\n{data.decode('utf-8')}")