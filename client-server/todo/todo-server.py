# todo-server.py

import socket

HOST = "0.0.0.0"  # binding to all network interfaces
PORT = 60000  # Port to listen on (non-privileged ports are > 1023)

file = "todo_list.txt"

#region read & write to file functions

def append_todo(todo,filename):
    '''Takes in a todo string and a file and writes the todo to the file on a new line.'''
    with open(filename, "a") as f:
        f.write(f'_{todo}\n') # note the underscore. this means it's not complete.

def read_file(filename):
    '''Takes in a filename and returns the contents of the file as a string'''
    with open(filename, "r") as f:
        return f.read().splitlines()
    
def get_undone_todos(filename):
    '''returns a list of todo's with the _ as the first character'''
    all_todos = read_file(filename)
    
    undone_todos = []
    for todo in all_todos:
        if todo[0] == "_":
            undone_todos.append(todo[1:])

    return undone_todos
    

def mark_todo_complete(filename, todo):
    with open(filename, 'r') as file:
        lines = file.readlines()

    line_found = False
    for i in range(len(lines)):
        if lines[i].strip() == f'_{todo}':
            lines[i] = f'X{todo}' + '\n'
            line_found = True
            break

    if not line_found:
        print("Line not found in the file.")
        return

    with open(filename, 'w') as file:
        file.writelines(lines)

    
#endregion  


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Waiting for a connection...")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        welcome_message = f'Welcome to the to-do list.' + \
                          f'\nEnter "1" to view todo list, ' + \
                          f'\n"2" to add a to-do item to the list, ' + \
                          f'\n"3" to mark a to-do as complete, ' + \
                          f'\nor "Quit" to quit.'
        
        conn.sendall(welcome_message.encode())

        #region functions for the socket

        def send_todo_list():
            '''sends client todo list'''
            todo_list = get_undone_todos(file)

            # first, let the client know how many lines to expect.
            line_count = len(todo_list)

            empty = False

            if line_count == 0:
                empty = True
                conn.sendall("1".encode())
            else:
                conn.sendall(str(line_count).encode())

            # recieve the ok to move on
            conn.recv(1024)

            # second, send that many lines to the client.
            if empty:
                conn.sendall("todo list is empty!".encode())
                # get the ok
                conn.recv(1024)
            else:
                for line in todo_list:
                    conn.sendall(line.encode())
                    # get the ok to send another
                    conn.recv(1024)

        def add_todo():
            '''add's a todo to the file'''
            # first, get a todo from the client
            todo = conn.recv(1024).decode()

            # add the todo to the file
            append_todo(todo, file)

        def complete_todo():
            '''complete's a todo from the file'''

            # first, send the todo list to look at:
            send_todo_list()

            # second, tell the client if it's empty:
            if len(get_undone_todos(file)) == 0:
                conn.sendall('empty'.encode())
            else:
                conn.sendall('full'.encode())

            # pass everything if there are no todos in the list
            if len(get_undone_todos(file)) != 0:

                # third, receive the todo they want to complete
                todo = ""
                while True:
                    todo = conn.recv(1024).decode()

                    # Check if todo is in the list
                    undone_todos = get_undone_todos(file)
                    valid = False
                    for item in undone_todos:
                        if todo == str(item):
                            valid = True
                            break

                    if valid:
                        conn.sendall('0'.encode())
                        break
                    else:
                       conn.sendall('1'.encode())

                # Mark that todo as complete.
                mark_todo_complete(file,todo)

                

        #endregion

        while True:
            choice = conn.recv(1024)

            if choice.decode() == "quit" or choice.decode() == "Quit":
                conn.sendall(b"Quitting...")
                break

            elif choice.decode() == '1':
                # view to-do list
                conn.sendall(b"Here's your to-do list.")
                send_todo_list()
                
            elif choice.decode() == '2':
                # add a to-do
                conn.sendall(b"Please enter the to-do you would like to add.")
                add_todo()

            elif choice.decode() == '3':
                # mark a to-do as complete
                conn.sendall(b"Which to-do did you complete?")
                complete_todo()

            else:
                conn.sendall(b'error')

            conn.sendall(b"What is your input? (1. view, 2. add, or 3. mark )")

