# Overview

"Todo" is a client-server networking program where the client can access a todo list that is kept on the server. The client has three options: view todo list, add a new todo, or mark a todo as complete.

To use this software, first configure the client file with the server's hostname as the "HOST" variable. Second, run the todo-server.py script on the server machine. The server will wait for a connection with the client. Then, run the todo-client.py script on the client machine. You should see a message on the server side saying that the connection has been made successfully. If you can't get a connection, check the firewall on either device and possibly disable it temporarily. Then, follow the instructions that display on the client side to view the todo list, add a todo, or mark a todo as done.

The todo list will be saved on the server machine in the "todo-list.txt" file.

I wrote this software to teach myself how to use the python socket library, specifically how to create a client-server network that handles multiple different requests.

For a visual demonstration of my software, check out my [Software Demo Video](https://youtu.be/I_UqZxQYhME).

# Network Communication

{Describe the architecture that you used (client/server or peer-to-peer)}
This software uses client-server architecture and TCP connection. (for more information, see the notes.md file). Also the program uses port number 60,000. The messages sent between the client and the server are just displayed on the command line or terminal. This program is designed to run on the terminal and has no GUI (for now.)

# Development Environment

I developed this software in python and using the VSCode IDE. To test this program, I used a virtual machine running Linux in VirtualBox (free virtual machine software).

I used the socket python library for this project, which is included in the python standard libraries. 

# Useful Websites

* [Very nice client-server tutorial to get started on RealPython](https://realpython.com/python-sockets/#echo-client-and-server)
* [How to set up Linux on VirtualBox](https://www.youtube.com/watch?v=rJ9ysibH768)
* [Basic socket video tutorial](https://www.youtube.com/watch?v=Lbfe3-v7yE0&t=17s)

# Future Work

* Make it a little more reliable even if the internet isn't great. Maybe add something that resets after it hangs for a few seconds.
* Add support for multiple clients to access the todo list at once using the "threading" library
* Test it on MacOS (this was only tested on Windows and Linux)
* Create a GUI for better user experience
