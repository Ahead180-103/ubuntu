
from socket import *
from time import sleep

s = socket(AF_INET,SOCK_DGRAM)

server_addr = ('192.168.192.255',9999)
#s.bind(('192.168.192.255',9999))
print('broadcast server port:',9999)

s.getsockopt(SOL_SOCKET,SO_BROADCAST,1)
while True:
    sleep(1)
    data = input('enter your message:')
    if not data:
        break
    s.sendto(data.encode(),server_addr)

    data,addr = s.recvfrom(4096)
    print(data.decode(),'from:',addr)

s.close()