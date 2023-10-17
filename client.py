import socket

class Client:

    def __init__(self, sock=None):
        if sock is not None:
            self.sock_ = sock
        else:
            self.sock_ = socket.socket()

    def register(self, host, port):
        self.sock_.connect((host, port))

    def listen_to_morfeus(self):
        received_data = self.sock_.recv(1024).decode('utf8')
        return received_data

    def respond_to_morfeus(self, msg):
        self.sock_.send(msg.encode('utf8'))

    def interact_with_user(self):
        state = "not_registered"
        while True:
            if state == "not_registered":
                action = input().split()
                if action[0] == "R":
                    self.register(action[1], int(action[2]))
                    state = "listening"

            if state == "responding":
                action = input().split()
                if action[0] == "M":
                    self.respond_to_morfeus(action[1])
                elif action[0] == "S":
                    msg = "No response"
                    self.respond_to_morfeus(msg)
                state = "listening"

            if state == "listening":
                received_data = self.listen_to_morfeus()
                if received_data:
                    state = "responding"
                    print("Received private message: ", received_data)
                    print("Please enter message or S to skip")


c = Client()
c.interact_with_user()