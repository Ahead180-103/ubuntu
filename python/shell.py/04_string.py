#!/usr/bin/python3

'''
字符串编码转换函数
ord(c)  返回一个字符串的Unicode编码
chr(i)  返回Unicode编码的对应字符
如：
  print(ord('A'))  返回65
  print(chr(65))   返回A
'''

s=input("请输入任意字符串: ")
if s != '':
 n=s[0]
 print("字符串中第一个字符的编码是: ",ord(n))


s=int(input("请输入一个数子(0~65535): "))
#n=chr(s)
print("对应的值是: ",chr(s))
