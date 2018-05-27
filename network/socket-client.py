import socket
import sys

#create TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define host
host = "localhost"

# define the communication port
port = 8080

# Connect the socket to the port where the server is listening
s.connect((host, port))
print("connection")

s.send(b"Hello World")
data = s.recv(1024)
s.close()
print("recv="+ repr(data))



