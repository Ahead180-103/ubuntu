#!/usr/bin/python3

from threading import Thread
from time import sleep,ctime
import os
from  signal import *

print('process pid:',os.getpid())

def test(sec):
    for i in range(5):
        sleep(sec)
        print('test mythread.....')




class mythread(Thread):
    def __init__(self,target,args = (),kwargs = {},name = 'Yolanda'):
        #Thread.__init__(self)
        super().__init__()
        self.name = name
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        print('use  thread  ......')
        self.target(*self.args)


t = mythread(target = test,args = (3,)) 

t.start()
#获取名字
print(t.name)
#修改名字
t.setName('Odven')
print(t.name)
t.join()
print(t.name)

print('process over')
