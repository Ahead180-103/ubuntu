#!/usr/bin/python3

from multiprocessing import Process
import os

size = os.path.getsize('./img.png')
print(size)

#复制上半部分
def copy1(filename):
    fr = open(filename,'rb')
    n = size // 2
    fw = open('a.png','wb')
    while True:
        if n < 1024:
            data = fr.read(n)
            fw.write(data)
            break
        data = fr.read(1024)
        fw.write(data)
        n -= 1024
    fr.close()
    fw.close()

#复制下半部分
def copy2(filename):
    fr = open(filename,'rb')
    fw = open('b.png','wb')
    fr.seek(size // 2,0)
    
    while True:
        data = fr.read(1024)
        if not data:
            break
        fw.write(data)
    fr.close()
    fw.close()

p1 = Process(target=copy1,args=('img.png',))
p2 = Process(target=copy2,args=('img.png',))

p1.start()
p2.start()

p1.join()
p2.join()













