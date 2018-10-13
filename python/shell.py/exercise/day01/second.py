#!/usr/bin/python3

'''
分三次输入当前的小时，分钟，秒数，
在终端打印已距离凌晨0：0：0过了多少秒
'''

s=input("请输入小时: ")
hour=int(s)
s=input("请输入分钟: ")
minute=int(s)
s=input("请输入秒: ")
second=int(s)

second=hour*3600+minute*60+second
print("距离0：0：0已过了",second,"秒")
