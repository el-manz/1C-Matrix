import socket

class Morfeus:

    def __init__(self, host, port, num_clients):
        self.socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_.bind((host, port))
        self.num_clients_ = num_clients
        self.socket_.listen(num_clients)
        self.client_sockets_ = []

    def register_clients(self):
        (client_socket, address) = self.socket_.accept()
        print("Connected: ", address)
        self.client_sockets_.append((client_socket, address))

    def get_clients_list(self):
        return self.client_sockets_

    def send_private_message(self, desired_client_socket, msg):
        desired_client_socket.send(msg.encode('utf8'))
        received_data = desired_client_socket.recv(1024).decode('utf8')
        return received_data

    def send_broadcast_message(self, msg):
        received_data = []
        for client_socket in self.client_sockets_:
            client_socket[0].send(msg.encode('utf8'))
            received_data.append(client_socket[0].recv(1024).decode('utf8'))
        return received_data

    def exit(self):
        for client_socket in self.client_sockets_:
            client_socket[0].close()
        self.socket_.shutdown(socket.SHUT_RDWR)
        self.socket_.close()
        print("Morfeus closed")

    def interaction_with_user(self):
        state = "registering"
        while True:
            if state == "registering":
                for i in range(self.num_clients_):
                    self.register_clients()
                state = "awaiting message"
            if state == "awaiting message":
                action = input().split()
                if action[0] == "MP":
                    response = self.send_private_message(self.client_sockets_[int(action[1])][0], action[2])
                    print("Response received: ", response)
                elif action[0] == "MB":
                    responses = self.send_broadcast_message(action[1])
                    print("Responses received: ", responses)
                elif action[0] == "E":
                    self.exit()
                    break


m = Morfeus('localhost', 8076, 1)
m.interaction_with_user()