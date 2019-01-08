#!/usr/bin/python3


from multiprocessing import Process
import os
from time import sleep,ctime


print(ctime())
def test(arg):
    sleep(5)
    print(arg)
    print("the process %s is executing" % os.getpid())

p = Process(target=test,args=("haha",))
p.start()

print(os.getpid())
p.join()
print(ctime())

print("finish")

class MyProcess(Process):
    def __init__():
        super().__init__()
    def run(self):
        sleep(10)
        print("haha...",os.getpid())

n = MyProcess(target=test,args=("yolanda",))
n.start()
print(os.getpid())
n.join()
print(ctime())
print("主进程执行到了这里。。。。")
