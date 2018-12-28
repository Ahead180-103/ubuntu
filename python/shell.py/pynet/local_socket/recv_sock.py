

from socket import *
import os
from time import sleep

sock_file = './sock'
if os.path.exists(sock_file):
    print('file exists ')
    sleep(1)
    os.unlink(sock_file)
    print('remove file sock')
    sleep(3)


s = socket(AF_UNIX,SOCK_STREAM)
s.bind(sock_file)
s.listen(5)

while True:
    print('listen port ...')
    c,addr = s.accept()
    print('connection from',addr)
    while True:
        msg = c.recv(4096)
        if msg:
            print('receive client message:',msg.decode())
        else:
            c.close()
            break
        n =  c.send('receive your message'.encode())
        print('send {} bytes'.format(n))

s.close()
