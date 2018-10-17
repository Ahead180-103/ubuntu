#!/usr/bin/python3

'''
输入三科成绩，看最大值和最小值
'''

a=int(input("please your A chengji:"))
b=int(input("please your B chengji:"))
c=int(input("please your C chengji:"))
s=a
if b>s:
    s=b
if c>s:
    s=c
print('max number: ',s)
s=a
if b<s:
    s=b
if c<s:
    s=c
print('min number: ',s)



