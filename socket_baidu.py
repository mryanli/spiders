#!/usr/bin/python
# -*- coding:UTF-8 -*-

import socket

conn = socket.socket()

# conn.setblocking(False)


conn.connect(('www.baidu.com',80))

while True:
    try:
        conn.send('GET / HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n'.encode())
        break
    except:
        pass


page = ''
while True:
    try:
        response = conn.recv(1024)
        while response:
            page += response
            print(response.decode('utf-8'))
            try:
                response = conn.recv(1024)
            except:
                break
        break
    except:
        pass




with open('baidu.html','w') as f:
    f.write(page)


# conn.close()






