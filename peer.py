import socket
import threading

class Peer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connections = []

        # start the listening thread
        self.start()


    def connect(self, peer_host, peer_port):
        '''creates a connection between this peer and another peer'''
        try:
            connection = self.socket.connect((peer_host, peer_port))
            self.connections.append(connection)
            print(f'Connected to {peer_host}:{peer_port}')
        except socket.error as e:
            print(f'Failed to connect to {peer_host}:{peer_port}. Error: {e}')
            

    def listen(self):
        '''Listens for incoming connections'''
        self.socket.bind((self.host, self.port))
        self.socket.listen(10)
        print(f'Listening for connections on {self.host}:{self.port}')

        while True:
            connection, address = self.socket.accept()
            self.connections.append(connection)
            print(f'Accepted connection from {address}')


    def send_data(self, data):
        '''Sends data between peers'''
        for connection in self.connections:
            try:
                connection.sendall(data.encode())
            except socket.error as e:
                print(f'Failed to send data. Error: {e}')


    def start(self):
        '''Start the listening thread when the peer class is initialized'''
        listen_thread = threading.Thread(target=self.listen)
        listen_thread.start()
