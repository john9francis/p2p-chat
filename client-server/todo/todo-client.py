# todo-client.py

import socket
import threading

HOST = "John_Francis"  # The server's hostname or IP address
PORT = 60000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # receive welcome message:
    welcome = s.recv(1024)
    print(welcome.decode())

    while True:
        choice = input()

        s.sendall(choice.encode())
        server_response = s.recv(1024)

        print(server_response.decode())

        if server_response.decode() == "Quitting...":
            break
        if server_response.decode() == "Here's your to-do list.":
            # view todo list logic
            # receive the todo list and print it
            todo_list = s.recv(1024)
            print(todo_list)
            print('Press enter to continue: ')
            input()
            
        if server_response.decode() == "Please enter the to-do you would like to add.":
            # enter todo logic
            pass
        if server_response.decode() == "Which to-do did you complete?":
            # enter complete logic
            pass

        continue_message = s.recv(1024)
        print(continue_message)


