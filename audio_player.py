import socket
import sys
import glob
from pydub import AudioSegment
from pydub.playback import play


ts = glob.glob("/home/pi/team_?.*")

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
teamsound = AudioSegment.from_file(ts[0])

# Bind the socket to the port
server_address = ('0.0.0.0', 1338)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        data = connection.recv(255)
        if data is not None:
            if data == b'kdctf_play':
                play(teamsound)

    finally:
        # Clean up the connection
        connection.close()
