#!/usr/bin/python3

from multiprocessing import Process,Pipe
import time,os
import random

fd1,fd2 = Pipe()
'''
如果Pipe()这是默认为True，表示为双向管道fd1,fd2都可是读写
如果Pipe(false),表示为单向管道,fd1,fd2分别是读写
'''

def func1():
    for i in range(5):
        time.sleep(2)
        fd1.send("I'm gaoyong%s"%i)
        print("func1 send message:  I'm gaoyong%s"%i)
        print('func1 pid',os.getpid(),'parent pid',os.getppid())

def func2():
    for i in range(5):
        data = fd2.recv()
        if not data:
            break
        print('func2 pid',os.getpid(),'parent pid',os.getppid())
        print('func2 receive func1 message: ',data)
        print('######################')

p1 = Process(target = func1)
p2 = Process(target = func2)

print('process pid',os.getpid())

p1.start()
p2.start()

p1.join()
p2.join()
