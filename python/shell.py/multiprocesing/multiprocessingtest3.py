#!/usr/bin/python3

from multiprocessing import Process
import time,os,sys


def th(sec,name):
    time.sleep(sec)
    print("I'm %s"% name)
    print("I'm working...")

result = []
for i in range(10):
    p = Process(target=th,args=(int(sys.argv[1]),sys.argv[2]))
    result.append(p)
    p.daemon = True
    p.start()


time.sleep(30)
print("parent over")

#for i in result:
#    i.join()

print('process over')
