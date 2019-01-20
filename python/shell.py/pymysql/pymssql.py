

import pymssql
from time import sleep

con = pymssql.connect(server="192.168.192.64",port="1433",user="fangwei",password="ruanjian2018",database="ivps",login_timeout=3)

print('connection success......')

cursor = con.cursor()
print('create cursor  success......')

cursor.execute("select * from fangwei where FNUMBER_FAT='TP002801000'")
#cursor.execute("select count(*) from fangwei")

con.commit()
row = cursor.fetchall()
for i in row:
    print(i)

print(cursor.rowcount)
print(cursor.fetchall())

print('waiting sleep 3....')

sleep(3)
cursor.close()
con.close()
