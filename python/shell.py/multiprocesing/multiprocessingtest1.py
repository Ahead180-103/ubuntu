#!/usr/bin/python3


from multiprocessing import Process
import os
from time import sleep,ctime

def worker():
    sleep(5)
    print('子进程结束',ctime())

'''
create child process
'''
p = Process(name='test',target=worker)

p.start()
print('start time',ctime())
print('child name:',p.name)
print(p.is_alive())
print('child pid:',p.pid)
print('parent pid:',os.getpid())
sleep(4)
print('父进程结束',ctime())
p.join()
sleep(2)
print('process over')
print('end time',ctime())
