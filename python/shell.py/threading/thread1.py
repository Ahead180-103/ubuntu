#!/usr/bin/python3

from threading import Thread
from time import sleep,ctime
import os
from  signal import *

alarm(10)
print('process pid:',os.getpid())

def test(sec):
    while True:
        sleep(sec)
        print("test threading module")
        print('thread pid:',os.getpid())

t = Thread(target = test,args = (3,)) 

t.start()
t.join()
print('process over')
