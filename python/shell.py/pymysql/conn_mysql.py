
import pymysql

'''写一个连接数据库的配置文件'''
config = {
    'host':'www.svnup.cn',
    'port':3306,
    'user':'gyahead',
    'password':'gauyao1125',
    'database':'mytest',
    'charset':'utf8',
}
'''创建连接'''
conn = pymysql.connect(**config)
try:
    '''创建游标'''
    cursor = conn.cursor()

    '''创建一个sql语句的变量'''
    sql = "select * from test"

    '''执行sql语句'''
    cursor.execute(sql)

    data = cursor.fetchall()
    for i in data:
        print(i)

    conn.commit()
except Exception as er:
    print("提交失败,回滚",er)
    conn.rollback()
finally:
    print('关闭游标，关闭连接')
    cursor.close()
    conn.close()


