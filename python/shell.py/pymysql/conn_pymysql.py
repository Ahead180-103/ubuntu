#!/usr/bin/python3
# _*_ coding: utf8 _*_

import pymysql

config = {
     'host':'14.18.86.176',
     'port':3306,
     'user':'root',
     'password':'smok2015',
     'database':'test',
     'charset':"utf8",
}

conn = pymysql.connect(**config)

try:
    c1 = conn.cursor()
    #sql =  "create table test1(id int primary key auto_increment,name char(20) not null,age  tinyint unsigned default 0,sex set('boy','girl'))"
    #sql = "alter table test1 modify sex set('boy','girl','other') default 'boy'"
    #sql = "select * from test1"
    #sql = "create table test(id int primary key auto_increment,school char(50),class char(20),numbers tinyint)"
    sql = "insert into test values(null,%s,%s,11)"
    data = ('changde','renren')
    c1.execute(sql,data)
    c1.fetchall()
    print("insert success",c1.rowcount)

    sql1 = "insert into test1(id,name,age) values(null,%s,11)"
    data1 = [('dingyan'),('qingjinglian')]
    c1.executemany(sql1,data1)
    c1.fetchall()
    print("insert success",c1.rowcount)
    #for i in data:
    #    row=print(i)
    #print("success",row)
    conn.commit()
#except:
#    print("Failed sql_rollback")
#    conn.rollback()

finally:
    print("close")
    c1.close()
    conn.close()





