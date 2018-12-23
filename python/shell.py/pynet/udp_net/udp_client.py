#udp_client.py

from socket import *
import sys

if len(sys.argv) < 3:
    print('''
       argv  is error !!
       run as
       python3 udp_clinet.py 127.0.0.1 8888
       ''')
    raise

HOST = sys.argv[1]
PORT = int(sys.argv[2])
SERVER_ADDR = (HOST,PORT)
print('server port',SERVER_ADDR)

#创建套接字
s = socket(AF_INET,SOCK_DGRAM)

#SEND and RECEIVE
data = input('消息:')

#给服务器发送
s.sendto(data.encode(),SERVER_ADDR)

#收到服务器的消息
data,addr = s.recvfrom(1024)
print("从服务器收到:",data.decode())

#关闭
s.close()











