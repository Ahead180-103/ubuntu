#!/usr/bin/python3

from socket import *
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')

if len(sys.argv) < 3:
    print('''
        argv attr error
        run as
        ./tcp_srever1.py 127.0.0.1 8888
    ''')
    raise

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)


s = socket()
s.bind(ADDR)

s.listen(5)
while True:
    print('waiting client messsage...')

    c,addr = s.accept()
    print('connection from ',addr)
    while True:
        data = c.recv(1024)
        if not data:
            break
        print('receive client message',data.decode())
        n = c.send('收到你的消息！'.encode())
        print('send %s bytes' % n)
    c.close()

s.close() 





