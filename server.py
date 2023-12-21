#!/usr/bin/python3

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 888

server.bind((host, port))

server.listen(2)

while True:
    client, addr = server.accept()
    print("Got a connection from %s" % str(addr))
    msg = "Thank you for connecting\r\n"
    client.send(msg.encode('ascii'))
    client.close()