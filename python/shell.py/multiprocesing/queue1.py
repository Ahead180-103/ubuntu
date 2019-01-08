#!/usr/bin/python3

from multiprocessing import Process,Queue
import time

q = Queue(3)
'''
消息队列是先进先出
'''

q.put('Yolanda')
q.put('丁艳')
q.put('Odven')
time.sleep(0.01)
print('是否为空',q.empty())
print('是否为满',q.full())
print('队列中有多少条信息',q.qsize())
#def func1():
#    for i in range(5):
#        q.put(i) 
#
#p = Process(target = func1)
#p.start()
#p.join()

print(q.get())
time.sleep(0.01)
print('###########################')
print('是否为空',q.empty())
print('是否为满',q.full())
print('队列中有多少条信息',q.qsize())



