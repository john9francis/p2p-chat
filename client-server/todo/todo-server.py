# echo-server.py

import socket

HOST = "0.0.0.0"  # binding to all network interfaces
PORT = 60000  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Waiting for a connection...")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        action1 = "view to-do list"
        action2 = "add a to-do"
        action3 = "mark a to-do as complete"

        welcome_message = f'Welcome to the to-do list.' + \
                          f'\nEnter "1" to {action1}, ' + \
                          f'\n"2" to {action2}, ' + \
                          f'\n"3" to {action3}, ' + \
                          f'\nor "Quit" to quit.'
        conn.sendall(welcome_message.encode())

        while True:
            data = conn.recv(1024)

            if data.decode() == "quit" or data.decode() == "Quit":
                conn.sendall(b"Quitting...")
                break
            else:
                conn.sendall(b'You said: ' + data + b'.')

