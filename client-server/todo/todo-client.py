# todo-client.py

import socket

HOST = "John_Francis"  # The server's hostname or IP address
PORT = 60000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # receive welcome message:
    welcome = s.recv(1024)
    print(welcome.decode())

    #region socket functions

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


    def add_todo():
        '''deals with adding a todo to the server's todo list'''
        # first, tell the server what todo to add
        todo = input()
        s.sendall(todo.encode())

    def complete_todo():
        '''accesses a todo from the server and changes it to complete'''
        # first, get a list of the todos
        receive_todo_list()

        # second, get input until they enter a valid todo
        while True:
            todo_to_mark = input()
            s.sendall(todo_to_mark.encode())

            response = s.recv(1024).decode()
            if response == '0':
                print(f"Marking {todo_to_mark} as complete.")
                break
            elif response == '1':
                print("Invalid option. Please try again.")





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
            complete_todo()

        elif server_response.decode() == "error":
            print("Sorry, invalid input. Please try again.")

        continue_message = s.recv(1024)
        print(continue_message.decode())

    


