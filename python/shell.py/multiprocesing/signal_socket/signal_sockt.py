#!/usr/bin/python3

from socket import *
from multiprocessing import Process,Semaphore
import time
import os,signal


local_socket = "./socket.txt"
if os.path.exists(local_socket):
    os.unlink(local_socket)

pid = os.getpid()
print(pid)

s = socket(AF_UNIX,SOCK_STREAM)
s.bind(local_socket)
s.listen(5)
c,addr = s.accept()
data = c.recv(1024).decode()
print(data)
s.close()

time.sleep(10)
os.kill(int(data),signal.SIGKILL)


print('start time:',time.ctime())

