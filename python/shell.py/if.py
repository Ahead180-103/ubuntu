#!/usr/bin/python3


'''
此实例用if判断奇偶数
输入一个数，让计算机判断这个数是偶数还是奇数
'''
s=input("请输入数字: ")
n=int(s)

if n%2 == 0:
   print("你输入的是偶数: ",n)
else:
   print("你输入的是奇数: ",n)

