#!/usr/bin/python3

'''
打印输入字符串的第一个字符和最后一个字符
如果是奇数打印中间的字符
如果是偶数不答应
'''

s=input("请输入随意字符串: ")
print(s[0])
print(s[-1])
lenth=len(s)%2
if lenth%2==1:
 center_index=len(s)//2
 print("字符串中间字符是: ",s[center_index])
else:
 print(len(s))
