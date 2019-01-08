#!/usr/bin/python3

from multiprocessing import Process,Semaphore
import time,os

#创建一个信号量初始值为 5
a = Semaphore(5)

#减少一个数
a.acquire()
a.acquire()

#增加一个数
a.release()

print(a.get_value())

