# echo-client.py
# from realpython.com

import socket

HOST = "2603:6080:8200:9922:e814:7730:5b5e:146e"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")
