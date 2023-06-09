# Overview

{Provide a description the networking program that you wrote. Describe how to use your software.  If you did Client/Server, then you will need to describe how to start both.}

{Describe your purpose for writing this software.}

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

{Describe the architecture that you used (client/server or peer-to-peer)}

### Client/server vs. peer-to-peer

Client/server networking is when everyone in the network connects to one big computer (the client). This method is more secure and scalable but more expensive.

Peer-to-peer networking is when all the computers connect to eachother. Each machine acts as both the client and the server. This method is easier and cheaper especially for small projects.

In this project I will be using Peer to peer networking. The reason I chose this method is because it's easy to set up, and it works across different operating systems.

{Identify if you are using TCP or UDP and what port numbers are used.}

### TCP vs. UDP

TCP (transmission control protocol) is used when you are sending more important information that you don't want to lose any bit of. For example, photos, messages, or documents.

UDP (user datagram protocol) is used when speed is more important than all the information. For example, with a broadcast, you might miss out on a half-second of content, but your main priority is to keep up with what's being said. 

In this project I will be using TCP, because when sending messages, information is more important then speed. 

{Identify the format of messages being sent between the client and server or the messages sent between two peers.}

### Format:

The messages being sent in this project are friendly informal text messages. 

# Development Environment

{Describe the tools that you used to develop the software}

I coded this project in Python using VSCode. 

{Describe the programming language that you used and any libraries.}

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [TCP vs. UDP complete guide](https://www.avast.com/c-tcp-vs-udp-difference)
* [Client-server vs. Peer-to-peer network models](https://www.networkstraining.com/peer-to-peer-vs-client-server-network/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Item 1
* Item 2
* Item 3