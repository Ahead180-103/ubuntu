#!/usr/bin/python3


from multiprocessing import Pool
import os
import time 

def worker(fn):
    time.sleep(1)
    print('pool map over...')
    print(time.ctime())
    return fn * fn

print(time.ctime())
p = Pool(4)

r = p.map(worker,range(10))

print(r)
p.close()
p.join()

print('process over')
print(time.ctime())
