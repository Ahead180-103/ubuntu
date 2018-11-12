#!/usr/bin/python3

def recursion(i):   #定义函数
    print(i)
    if i/2 > 1:   #判断递归条件，退出
         recursion(i/2)  #递归函数自身
    print('返回值:',i)

recursion(10)
