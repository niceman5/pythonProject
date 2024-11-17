import socket
from _thread import *

# 소켓으로 접속할 서버의 IP와 PORT를 지정한다
HOST = "localhost"
PORT = 9999

# Connect the socket to the port where the server is listening
# create TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


def recv_data(client_socket):
    while True:
        data = client_socket.recv(1024)
        print("recv = " + repr(data.decode()))

start_new_thread(recv_data, (client_socket,))
print("connection")

while True:
    message = input()
    if message == 'quit':
        close_data = message
        break

    client_socket.send(message.encode())

client_socket.close()
