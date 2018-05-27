import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#define host
host = "localhost"

# define the communication port
port = 8080

# Bind the socket to the port
sock.bind((host, port))

#Listen for incoming connections
sock.listen(1)

# Wait for a connection
print('waiting for a connection')

conn, client = sock.accept()

print('Connected by = ', client)

while True:
    data = conn.recv(1024)
    if not data:
        break
    print("recv = " + repr(data))
    conn.send(data)

conn.close()