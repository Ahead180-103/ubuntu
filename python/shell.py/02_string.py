#!/usr/bin/python3

'''
输入任意字符串，判断这个字符串是不是回文
回文是指中心对称的文字
如：
  上海自来水来自海上
  abcba
'''

s=input("请输入字符串:")

reverse_string = s[::-1]  #把字符反过来
print(reverse_string)
if  reverse_string == s:
  print(s,"是回文")
else:
  print(s,"不是回文")
