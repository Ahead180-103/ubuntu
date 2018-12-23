#udp_server.py

from socket import *
import sys

#从命令行传入IP and PORT
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)
print('server port',ADDR)
#创建套接字
s = socket(AF_INET,SOCK_DGRAM)

#绑定IP and PORT
s.bind(ADDR)

#RECV and SEND message
data,addr = s.recvfrom(1024)
print('receive from %s:%s' % (addr,data.decode()))

s.sendto("收到你的消息".encode(),addr)


#关闭
s.close()
