
from socket import *
from time import sleep

s = socket(AF_INET,SOCK_DGRAM)

s.bind(('',9999))
print('broadcast listen port:',9999)

s.getsockopt(SOL_SOCKET,SO_BROADCAST,1)
while True:
    try:
        sleep(1)
        data,addr = s.recvfrom(4096)
        print('receive client message:',data.decode(),'from:',addr)

        s.sendto('receive your message'.encode(),addr)
    except IOError as er:
        print('退出',er)
        break

s.close()