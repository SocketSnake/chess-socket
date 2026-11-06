import socket

class Server:
    def __init__(self, ip_addr: str, port: int):
        self.ip_addr = ip_addr
        self.port = port

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip_addr, port))
        
        self.server_socket.listen(5)

    def get_server_data(self):
        pass

    def send_server_data(self):
        conn, addr = self.server_socket.accept()
        while True:
            print(f"Клиент {addr}, подключился")
            data = conn.recv(1024)
            if not data:
                break
            print(f"Клиент отправил сообщение: {data.decode('utf-8')}")

            conn.sendall(f"Привет твое сообщение:\n{data.encode('utf-8')}")

            self.server_socket.close()
