#tcp server.py

from socket import *

#创建tcp套接字
sockfd = socket(AF_INET,SOCK_STREAM)

#绑定ip and port
sockfd.bind(('127.0.0.1',8888))

#监听
sockfd.listen(5)
while True:
    #等待接受客服端的连接
    print("waiting for connect ...")
    connfd,addr = sockfd.accept()
    print("connect form", addr)
    while True:
        #接受
        data = connfd.recv(1024)
        if not data:
            break
        print('receive message >>',data.decode())
            
        #发送
        n = connfd.send(b'receive your message\n')
        print('send %d bytes data' % n)
     
    #关闭
    connfd.close()
sockfd.close()
