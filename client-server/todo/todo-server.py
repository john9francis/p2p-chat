# echo-server.py

import socket

HOST = "0.0.0.0"  # binding to all network interfaces
PORT = 60000  # Port to listen on (non-privileged ports are > 1023)

file = "todo_list.txt"

# functions we will be using to modify the todo list
def write_todo(todo,filename):
    '''Takes in a todo string and a file and writes the todo to the file on a new line.'''
    with open(filename, "w") as f:
        f.write(todo)
        f.write('\n')

def read_file(filename):
    '''Takes in a filename and returns the contents of the file as a string'''
    with open(filename, "r") as f:
        return filename.read()



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    print("Waiting for a connection...")
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")

        view = "view to-do list"
        add = "add a to-do"
        complete = "mark a to-do as complete"

        welcome_message = f'Welcome to the to-do list.' + \
                          f'\nEnter "1" to {view}, ' + \
                          f'\n"2" to {add}, ' + \
                          f'\n"3" to {complete}, ' + \
                          f'\nor "Quit" to quit.'
        conn.sendall(welcome_message.encode())

        while True:
            data = conn.recv(1024)

            if data.decode() == "quit" or data.decode() == "Quit":
                conn.sendall(b"Quitting...")
                break
            if data.decode() == '1':
                # view to-do list
                pass
            if data.decode() == '2':
                # add a to-do
                pass
            if data.decode() == '3':
                # mark a to-do as complete
                pass

            else:
                conn.sendall(b'Sorry, That\'s not an option. Please try again.')

