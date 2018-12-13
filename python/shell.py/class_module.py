#!/usr/bin/python3
#__*__ coding: utf-8 __*__


class play:
    def __init__(self,name,sex,age,cszdl=1000):
        self.name=name
        self.sex=sex
        self.age=age
        self.cszdl=cszdl
    def a(self,cj):
        print(cj)
    def add_b(self,add):
        print("增长",add,"战斗力")
    def remove_b(self,remove):
        print("消耗",remove,"战斗力")
    def view_info(self):
        print("姓名:",self.name,"性别:",self.sex,"年龄:",self.age,"初始战斗力:",self.cszdl)

human1=play("苍井井","女",18)
human1.view_info()
human1.remove_b(200)

human1=play("东尼木木","男",20,1800)
human1.view_info()
human1.add_b(100)
