import socket

class Client:

    def __init__(self, sock=None):
        if sock is not None:
            self.sock_ = sock
        else:
            self.sock_ = socket.socket()

    def register(self, host, port):
        self.sock_.connect((host, port))
        # received_data = self.sock_.recv(1024).decode('utf8')
        # print(received_data)
        # assert received_data == "Client is registered~"

    def listen_to_morfeus(self):
        # data = ""
        # msg_queue = []
        while True:
            received_data = self.sock_.recv(1024).decode('utf8')
            # data += received_data
            # msg_queue = data.split('~')
            # if
            if not received_data:
                break
            print(received_data)
            # self.sock_.send("Message received".encode('utf8'))
            msg = "DFSD"
            self.respond_to_morfeus(msg)

    def respond_to_morfeus(self, msg):
        self.sock_.send(msg.encode('utf8'))


c = Client()
c.register('localhost', 8083)
c.listen_to_morfeus()