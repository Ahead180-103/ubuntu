#!/usr/bin/python3

'''
商店搞活动购买大于100优惠20
'''
money=int(input("请输入总数: "))
pay=money - 20 if money > 100  else money
print("你应付",pay,"元")
