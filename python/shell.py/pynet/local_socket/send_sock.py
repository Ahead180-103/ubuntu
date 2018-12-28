

from socket import *
import os
from time import sleep

sock_file = './sock'
#if os.path.exists(sock_file):
#    print('file exists ')
#    sleep(1)
#    os.unlink(sock_file)
#    print('remove file sock')
#    sleep(3)

s = socket(AF_UNIX,SOCK_STREAM)
s.connect(sock_file)

while True:
    msg = input('enter your message:')
    if msg:
        s.send(msg.encode())
    else:
        s.close()
        break
    data = s.recv(1024)
    print('receive server message:',data.decode()) 

s.close()
