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

    #region Functions

    def receive_todo_list():
        '''deals with receiving and displaying the todo list from the server'''

        # first, receive the amount of lines
        list_lines = int(s.recv(4096).decode())

        # send the ok to move on
        s.sendall(b'ok')

        # second, receive that many lines from the server.
        for _ in range(list_lines):
            line = s.recv(4096).decode()
            print(line)

            # send the ok to send another
            s.sendall(b'ok')

        # third, send back something
        s.send(b'done')

    def add_todo():
        '''deals with adding a todo to the server's todo list'''
        # first, tell the server what todo to add
        todo = input()
        s.sendall(todo.encode())

    #endregion

    while True:
        choice = input()

        s.sendall(choice.encode())
        server_response = s.recv(1024)

        print(server_response.decode())

        if server_response.decode() == "Quitting...":
            break

        elif server_response.decode() == "Here's your to-do list.":
            receive_todo_list()

        elif server_response.decode() == "Please enter the to-do you would like to add.":
            add_todo()

        elif server_response.decode() == "Which to-do did you complete?":
            # enter complete logic
            pass

        elif server_response.decode() == "error":
            print("Sorry, invalid input. Please try again.")
            break

        continue_message = s.recv(1024)
        print(continue_message.decode())

    


