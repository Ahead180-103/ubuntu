#!/usr/bin/python3

from pymongo import MongoClient
import bson.binary

conn = MongoClient('127.0.0.1',27017)

db = conn.admin
db.authenticate(name='root', password='gauyao1125')

db = conn.image

myset = db.jpg

#with open('smok.jpg','rb') as f:
#    while True:
#        data = f.read(4096)
#        if not data:
#            break
#        content = bson.binary.Binary(data)
#        myset.insert({'filename':'file.jpg','data':content})
#

with open('smok.jpg','rb') as f:
        content = bson.binary.Binary(f.read())
        myset.insert({'filename':'file.jpg','data':content})

conn.close()




