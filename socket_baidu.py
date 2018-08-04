#!/usr/bin/python
# -*- coding:UTF-8 -*-

import socket

conn = socket.socket()


conn.connect(('www.baidu.com',80))



conn.send('GET / HTTP/1.1\r\nHost:www.baidu.com\r\n\r\n'.encode())

page = ''

response = conn.recv(1024)
while response:
    page += response.decode('utf-8')
    print(response.decode('utf-8'))

    response = conn.recv(1024)
    conn.setblocking(0)



with open('baidu.html','w') as f:
    f.write(page)


# conn.close()






