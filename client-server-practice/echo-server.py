# echo-server.py
# from realpython.com

import socket

HOST = "0.0.0.0"  # Trying to bind to all network interfaces
PORT = 60000  # Port to listen on (non-privileged ports are > 1023)

# three requests that the server can respond to
request1 = "Echo"
request2 = "Tell a joke"
request3 = "Access a database"

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Waiting for a connection...")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            welcome_message = f"Would you like me to... \n1.{request1}, \n2.{request2}, \n3.{request3}, or \n4. Quit? " + '\n(Please enter "1", "2", or "3".)'

            conn.sendall(welcome_message.encode())

            data = conn.recv(1024)

            conn.sendall(b'You chose: ' + data + b'.')

            if data.decode() == "1":
                # do response1
                pass
            if data.decode() == "2":
                # do response2
                pass
            if data.decode() == "3":
                # do response3
                pass
            if data.decode() == "4":
                break
            else: 
                # throw an error
                pass