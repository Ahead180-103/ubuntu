#!/usr/bin/python3

from multiprocessing import Process
import threading
import time,os

def test(i):
    time.sleep(10)
    print('say hi',i,'  child pid: ',os.getpid(),'    parent pid: ',os.getppid())

#多进程
process = []

for i in range(10):
    p = Process(name=test,target=test,args=(i,))
    process.append(p)
    p.start()

for i in process:
    i.join()


print('#####################')
#单进程
for i in range(10): 
    test(i)
