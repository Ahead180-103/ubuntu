
from socket import *

#创建套接字
s = socket()

#发起连接请求
s.connect(('127.0.0.1',8888))

#发送消息bytes格式
data = input('send >>')
s.send(data.encode())

#接受消息
data = s.recv(1024).decode()
print(data)

#关闭套接字
s.close()

