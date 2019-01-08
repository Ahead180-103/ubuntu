#!/usr/bin/python3


from multiprocessing import Pool
import os
import time 

def worker():
    sleep(5)
    print('子进程结束',ctime())

'''
create child process
'''
#iterstor = [1,2,3,4,5]
#p = Pool(4)
#
#r = p.map(worker,iterstor)
#
#p.close()
#p.join()
#
#print('process over')
#
#for i in r:
#    print(i)
#

def run(fn):
    time.sleep(1)
    return fn*fn

test = [1,2,3,4,5,6,7,8,9]

s = time.time()
for fn in test:
    run(fn)
e = time.time()
print('for 执行时间:',e - s)

pool = Pool(3)

#使用该模块中的map融合了原map函数和该模块中apply_async函数
r = pool.map(run,test)
pool.close()
pool.join() 
e1 = time.time()
print('执行时间:',e1 - e)




