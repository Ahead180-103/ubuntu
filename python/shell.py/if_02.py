#!/usr/bin/python3

'''
商店搞活动购买大于100优惠20
'''
money=int(input("请输入总数: "))
pay=money - 20 if money >= 100  else money
print("你应付",pay,"元")



'''
输入任何数字都显示正数
'''

s=int(input("请输入任意数字: "))
s= -s  if s < 0 else s
print("你输入数字的绝对值是: ",s)
