#!/usr/bin/python3

'''
任意输入一个数
1、判断这个数是否大于100
2、判断这个数是否小于0
3、判断这个数是否在20～50之间
'''
s=input("请输入任意一个数: ")
n=int(s)

if n<0:
 print("这个数小于0")
elif n>100:
 print("这个数大于100")
elif 20<n<50:
 print("这个数在20～50之间")
else:
 print ("其他")
