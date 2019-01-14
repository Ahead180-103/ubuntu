#!/usr/bin/python3

from multiprocessing import Semaphore,Process
from time import sleep,ctime
import os

sem = Semaphore(3)

def func1(sec):
    print('start func1',os.getpid())
    sleep(1)
    print('func1 acquire',sem.acquire())
    sleep(sec)
    print('func1 release',sem.release())

def func2(sec):
    print('start func2',os.getpid())
    sleep(1)
    print('func2 acquire',sem.acquire())
    sleep(sec)
    print('func2 release',sem.release())

def func3(sec):
    print('start func3',os.getpid())
    sleep(1)
    print('func3 acquire',sem.acquire())
    sleep(sec)
    print('func3 release',sem.release())

def func4(sec):
    print('start func4',os.getpid())
    sleep(1)
    print('func4 acquire',sem.acquire())
    sleep(sec)
    print('func4 release',sem.release())

l = [func1,func2,func3,func4]
resulf = []

#观察四个进程的执行过程，和现象
for i in l:
    p = Process(target = i,args = (3,))
    resulf.append(p)
    p.start()

for i in resulf:
    i.join()

print('last semaphore number:',sem.get_value())
print('process over')









