#!/usr/bin/python3

from pymongo import MongoClient

#创建连接
#conn = pymongo.MongoClient('/tmp/mongodb-27017.sock')
conn = MongoClient('127.0.0.1',27017)

#进入数据库
db = conn.gyahead

#在数据库中验证用户，密码
db.authenticate(name='gy', password='gauyao1125')

#绑定集合
myset = db.test

#向集合中插入文档
#for i in range(5):
#    message = {'name':'gyy','age':30,'see':'Yolanda'}
#    print(message)
#    myset.insert(message)

#修改操作
#for i in range(3,15):
#    myset.update({'feel':{'$exists':False}},{'$set':{'feel':i}},upsert=True)

#删除文档
print(myset.delete_one({'feel':14}))

#删除索引
#index = myset.drop_indexes()

#创建索引
#index = myset.ensure_index('name',1)

#创建复合索引
#index = myset.ensure_index([('name',1),('age',1)])

#创建唯一索引，稀疏索引
#index = myset.ensure_index('feel',unique=True,sparse=True)

#查看索引
index = myset.list_indexes()
for i in index:
    print(i)

#查看集合中的文档
a = myset.find()
for i in a:
    print(i)

#关闭连接
conn.close()





