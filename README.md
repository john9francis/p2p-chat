# Overview

In this repository, I have several mini projects demonstrating the python socket and threading libraries. These libraries are used to create network connections between computers. 

# Network communication

There are a couple of different types of network communications demonstrated here. Client/server, peer-to-peer, TCP, and UDP (for definitions, see notes.md.) The project are orgaized into two folders: client-server and peer2peer. Inside these folders are various projects utilizing either TCP or UDP.

# Development Environment

I coded these projects in Python using VSCode. I used the socket and threading libraries that are built in to the python standard libraries. I also used VirtualBox to run a virtual machine for testing purposes. 

# Useful Websites

* [TCP vs. UDP complete guide](https://www.avast.com/c-tcp-vs-udp-difference)
* [Client-server vs. Peer-to-peer network models](https://www.networkstraining.com/peer-to-peer-vs-client-server-network/)
* [Some socket and threading functions to get started](https://medium.com/@luishrsoares/implementing-peer-to-peer-data-exchange-in-python-8e69513489af)
* [Very nice client-server tutorial to get started on RealPython](https://realpython.com/python-sockets/#echo-client-and-server)
* [How to set up Linux on VirtualBox](https://www.youtube.com/watch?v=rJ9ysibH768)
* [Basic socket video tutorial](https://www.youtube.com/watch?v=Lbfe3-v7yE0&t=17s)

# Completed Projects:

* [Echo](client-server/echo): client sends something to the server and the server repeats it right back
* [Todo](client-server/todo): server holds a todo list which the client can modify in three different ways

# Future Work

* Basic peer-to-peer chat network
* Server that can handle many clients simultaneously
* Video game network using UDP
