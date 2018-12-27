

from socket import *


s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',8888))
s.listen(5)

while True:
    print('waiting client connection....')
    c,addr = s.accept()
    print('connection from:',addr)
    f = open('test.docx','wb')
    while True:
        data = c.recv(4096)
        if not data:
            break
        print('receive client data:',data)
        f.write(data)
        print('insert text success')
    f.close()
    c.close()
s.close()