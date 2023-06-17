# Notes about python sockets:

**Host:** A host is a device connected to the network. To define a host in code, use the device's IP address.

**Port:** A port is like a numbered gate on a computer that allows different programs to send and receive information over a network. We can use different ports to do different functions. For example, maybe port 2000 echo's what you say and port 2001 accesses something from the servers database. 

### Client/server vs. peer-to-peer

**Client/server** networking is when everyone in the network connects to one big computer (the client). This method is more secure and scalable but more expensive.

**Peer-to-peer** networking is when all the computers connect to eachother. Each machine acts as both the client and the server. This method is easier and cheaper especially for small projects.

### TCP vs. UDP

**TCP** (transmission control protocol) is used when you are sending more important information that you don't want to lose any bit of. For example, photos, messages, or documents.

**UDP** (user datagram protocol) is used when speed is more important than all the information. For example, with a broadcast, you might miss out on a half-second of content, but your main priority is to keep up with what's being said.
