#!/usr/bin/python3

'''
True and True     #是Ture
True and False    #是False
False and True    #是False
False and False  #是False
'''

'''
True or True     #是Ture
True or False    #是Ture
False or True    #是Ture
False or False  #是False
'''

s=input("请输成绩: ") or '0'
s=float(s)

if s>100 or s<0:
  print("成绩不合法")
else:
  print("你的成绩是: ",s)
