#!/usr/bin/python3


from multiprocessing import Pool
import os
from time import sleep,ctime

def worker(args):
    sleep(args)
    print('子进程结束',ctime())
    return '"over" %s'% args

'''
create child process
'''

print('Pool  start',ctime())
p = Pool(processes=4)
th = []

for i in range(10):
    r = p.apply_async(func=worker,args=(5,))
    th.append(r)

p.close()
p.join()
print('进程池关闭....')
print('Pool close',ctime())
#print(th)

for i in th:
    print(i.get())



