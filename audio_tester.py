import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 1338)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
# Send data
message = b"kdctf_play"
print('sending {!r}'.format(message))
sock.sendall(message)

