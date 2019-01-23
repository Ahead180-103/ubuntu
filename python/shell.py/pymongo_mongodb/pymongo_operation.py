#!/usr/bin/python3

#from pymongo import MongoClient
import pymongo

#创建连接
conn = pymongo.MongoClient('/tmp/mongodb-27017.sock')

#进入数据库
db = conn.gyahead

#在数据库中验证用户，密码
db.authenticate(name='gy', password='gauyao1125')

#绑定集合
myset = db.test

#向集合中插入文档
message = {'name':'gyy','age':30,'see':'Yolanda'}
print(message)
myset.insert(message)
myset.remove({'see':'Yolanda'})

a = myset.find()
for i in a:
    print(i)

#关闭连接
conn.close()
