#!/usr/bin/python3

'''
今年小明20周岁的生日，假设每年365天，
计算他过了多少哦个星期，余多少天
'''
age=20
days=age*365  #总共多少天
weeks=days//7  #多少星期
day=days%7  # 还剩多少天
print("小明过了:",weeks,
       "个星期,余",day,"天")
