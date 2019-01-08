#!/usr/bin/python3

from multiprocessing import Process,Queue
import time

#q = Queue()
#消息队列对消息数量没有限制
q = Queue(10)
#消息队列对消息数量有限制，为10条数据满了，然后在q.put是就会阻塞
'''
消息队列是先进先出
先到先得,得一个少一个
'''

for i in range(10):
    q.put(i) 
time.sleep(0.01)
print('是否为空',q.empty())
print('是否为满',q.full())
print('队列中有多少条信息',q.qsize())

def func1():
    while True:
        try:
            data = q.get_nowait()
            #上面为不阻塞获得消息队列中的数据，当队列中没有数据后会出现异常
            #data = q.get()
            #上面为阻塞获得消息队列中的数据，当队列中没有数据后会一直等待,阻塞
            print('process func1 ,get data :',data) 
            time.sleep(0.5)
        except:
            break

def func2():
    while True:
        try:
            data = q.get_nowait()
            #data = q.get()
            print('process func2 ,get data :',data) 
            time.sleep(0.5)
        except:
            break


p1 = Process(target = func1)
p2 = Process(target = func2)

p1.start()
p2.start()

p1.join()
p2.join()

print('###########################')
print('是否为空',q.empty())
print('是否为满',q.full())
print('队列中有多少条信息',q.qsize())



