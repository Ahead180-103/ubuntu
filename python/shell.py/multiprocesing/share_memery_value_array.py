#!/usr/bin/python3

from multiprocessing import Process,Value,Array
import time


#创建Value类型的共享内存，只能将一个数据存到共内存，下面相当于开辟了一个共享内存位置，并放了一个初始值 1
obj = Value('i',2000)
#从共享内存中取值
print(obj.value)


#创建Array类型的共享内存，可以将多个数据存到共内存，下面相当于开辟了3个共享内存位置，并放了3个初始值以列表的形式[1,2,3]
obj = Array('i',[1,2,3])
#从共享内存中取值
for i in obj:
    print(i)
