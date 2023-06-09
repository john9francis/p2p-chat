from peer import Peer
import time

# Create two peer instances
HOST1 = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT1 = 8001  # Port to listen on (non-privileged ports are > 1023)
PORT2 = 8002

peer1 = Peer(HOST1, PORT1)
peer2 = Peer('localhost', 8001)
