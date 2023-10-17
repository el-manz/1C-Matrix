import socket

class Morfeus:

    def __init__(self):
        self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_.bind(('', 8083))
        self.socket_.listen(5)
        self.client_sockets_ = []

    def register_clients(self):
        for i in range(1):
            (client_socket, address) = self.socket_.accept()
            print("Connected: ", address)
            self.client_sockets_.append((client_socket, address))
            # client_socket.send("Client is registered~".encode('utf8'))

    def get_clients_list(self):
        return self.client_sockets_

    def send_private_message(self, desired_client_socket, msg):
        desired_client_socket.send(msg.encode('utf8'))
        received_data = desired_client_socket.recv(1024).decode('utf8')
        print("Morfeus received: ", received_data)

    def send_broadcast_message(self, msg):
        for client_socket in self.client_sockets_:
            client_socket.send(msg.encode('utf8'))

    def exit(self):
        for client_socket in self.client_sockets_:
            client_socket[0].close()
        self.socket_.shutdown(socket.SHUT_RDWR)
        self.socket_.close()
        print("Morfeus closed")


m = Morfeus()
m.register_clients()
m.send_private_message(m.client_sockets_[0][0], 'abc')
m.send_private_message(m.client_sockets_[0][0], 'def')
m.exit()