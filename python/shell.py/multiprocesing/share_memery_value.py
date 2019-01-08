#!/usr/bin/python3

from multiprocessing import Process,Value,Array
import time,os
import random

#创建Value类型的共享内存，只能将一个数据存到共内存，下面相当于开辟了一个共享内存位置，并放了一个初始值 2000
obj = Value('i',2000)
#从共享内存中取值
print('初始值:',obj.value)
print('start time:',time.ctime())
print('process %s' % os.getpid())

def deposite():
    print('deposite process %s' % os.getpid())
    for i in range(100):
        obj.value += random.randint(0,200)
        time.sleep(0.05)

def withdraw():
    print('withdraw process %s' % os.getpid())
    for i in range(100):
        obj.value -= random.randint(0,200)
        time.sleep(0.04)


p1 = Process(target = deposite)
p1.start()
p2 = Process(target = withdraw)
p2.start()

p1.join()
p2.join()

print('最后剩余的值',obj.value)
print('close time:',time.ctime())
     
