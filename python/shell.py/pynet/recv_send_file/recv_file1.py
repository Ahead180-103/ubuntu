

from socket import *


s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

while True:
    try:
        print('waiting client connection....')
        c,addr = s.accept()
        print('connection from:',addr)
        #f = open('test.txt','wb')
        while True:
            #f = open('test.txt','wb')
            data = c.recv(4096)
            f = open('test.txt','ab')
            if not data:
                f.close()
                break
            print('receive client data:',data.decode())
            f.write(data)
            f.write('\n'.encode())
            print('insert text success')
            f.close()
    except KeyboardInterrupt as er:
        print('退出',er)
        break
    c.close()
s.close()
