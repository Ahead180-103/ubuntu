#!/usr/bin/python3


from pymongo import MongoClient
import gridfs


conn = MongoClient('127.0.0.1',27017)

db = conn.admin
db.authenticate(name='root', password='gauyao1125')

db = conn.grid

fs = gridfs.GridFS(db)

cursor = fs.find()

for file in cursor:
    print(dir(file))
    print(file.filename)
    with open('test.jpg','wb') as f:
        f.write(file.read())



conn.close()


