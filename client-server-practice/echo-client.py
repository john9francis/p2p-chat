# echo-client.py
# from realpython.com

import socket

HOST = "John_Francis"  # The server's hostname or IP address
PORT = 60000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # receive welcome message:
    welcome = s.recv(1024)

    print(welcome.decode())

    response = input()

    s.sendall(response.encode())
    data = s.recv(1024)

print("Received: " + data.decode())
