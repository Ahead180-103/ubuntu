#!/usr/bin/python3

from pymongo import MongoClient
import bson.binary
import os
from time import sleep

conn = MongoClient('127.0.0.1',27017)

db = conn.admin
db.authenticate(name='root', password='gauyao1125')

db = conn.image

myset = db.jpg

cursor = myset.find({'filename':'file.jpg'})


print(cursor)

def f_find():
    for i in cursor:
        with open(i['filename'],'ab') as f:
            f.write(i['data'])

if os.path.exists('./file.jpg'):
    print('file exists.....')
    sleep(2)
    os.remove('./file.jpg')
    print('remove file....')
    sleep(5)
    print('write file....')
    f_find()
else:
    f_find()

#for i in cursor:
#    print(i)
#print(dir(cursor))

print(cursor.count())

#cursor = myset.find()
#for i in cursor:
#    if i['filename'] == 'file.jpg':
#        print(i['data'])




conn.close()




