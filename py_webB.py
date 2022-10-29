#!/bin/env python3

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = "GET http://data.pr4e.org/romeo-full.txt HTTP/1.0\\n\\n".encode()
mysock.send(cmd)

while True:
    print("LOOP ENTERED\n")
    data = mysock.recv(512)
    if (len(data) < 1):
        print("No data")
        break
    print(data.decode())
mysock.close()
exit()

