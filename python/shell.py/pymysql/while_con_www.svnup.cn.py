
import pymysql
import sys
config = {
    'host':'www.svnup.cn',
    'port':3306,
    'user':"gyahead",
    'password':'gauyao1125',
#    'database':'test',
    'charset':'utf8',
    }
try:
    conn = pymysql.connect(**config)
except:
    print('connection failed')
    exit
cursor = conn.cursor()
while True:
    try:
        sql = input("enter sql command:")
        if not sql:
            break
        cursor.execute(sql)
        data = cursor.fetchall()
        for i in data:
            print(i)
        conn.commit()
    except Exception as er:
        print('failed rollback',er)
        conn.rollback()

print('close')
cursor.close()
conn.close()

