#!/usr/bin/python3

from multiprocessing import Process,Semaphore
import time
import os,signal


print('start time:',time.ctime())

#一个进程内只能有一个signal.alarm
signal.alarm(5)
time.sleep(2)
signal.alarm(10)

while True:
    time.sleep(1)
    print('waiting signal message ......',time.ctime())


print('close time:',time.ctime())
