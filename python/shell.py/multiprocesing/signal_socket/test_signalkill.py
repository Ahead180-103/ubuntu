#!/usr/bin/python3

from socket import *
from time import sleep
import os

local_socket = "./socket.txt"
if not os.path.exists(local_socket):
    print('local_socket  is not exiests')
  
pid = str(os.getpid())
s = socket(AF_UNIX,SOCK_STREAM)
s.connect(local_socket)
#s.listen(5)
print(pid)
s.send(pid.encode())

s.close()

print('process pid:',os.getpid())
while True:
    sleep(2)
    print('waiting to be killed....')

