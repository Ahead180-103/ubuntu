#!/usr/bin/python3

from multiprocessing import Process,Semaphore
import time
import os,signal


print('start time:',time.ctime())
e1 = time.time()

#一个进程内只能有一个signal.alarm
signal.alarm(5)

#阻塞信号
#signal.pause()

while True:
    e2 = time.time()
    e = e2 - e1
    print(e)
    time.sleep(1)
    if e > 30:
        print(e)
        break
    print('waiting signal message ......',time.ctime())
    #忽略signal.SIGALRM信号
    signal.signal(signal.SIGALRM,signal.SIG_IGN)
    #忽略signal.SIGINT信号
    signal.signal(signal.SIGINT,signal.SIG_IGN)


print('close time:',time.ctime())
