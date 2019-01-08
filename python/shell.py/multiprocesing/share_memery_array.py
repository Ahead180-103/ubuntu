#!/usr/bin/python3

from multiprocessing import Process,Value,Array
import time,os
import random

print('process pid:',os.getpid())

obj = Array('i',5)
for i in obj:
    print(i)

def fun(m,n):
    print('fun process pid %s' % os.getpid())
    for i in range(n):
        m[i] = i


p = Process(target = fun,args = (obj,5))
p.start()
p.join()
print('###########################################')
for i in obj:
    print(i)


def fun(m,n):
    print('fun process pid %s' % os.getpid())
    for i in range(n):
        m[i] = i
    m[2] = 520

p = Process(target = fun,args = (obj,5))
p.start()
p.join()
print('###########################################')
for i in obj:
    print(i)



