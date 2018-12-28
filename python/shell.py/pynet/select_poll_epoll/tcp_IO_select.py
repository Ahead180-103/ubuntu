
from socket import *
from select import select
s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

rlist = [s]
wlist = []
xlist = []

while True:
    print('listen port ....')
    rs,ws,xs = select(rlist,wlist,xlist)
    for i in rs:
        print(i)
        if i is s:
            c,addr = i.accept()
            print('connection from :',addr)
            rlist.append(c)
        else:
            data = i.recv(4096)
            if not data:
                i.close()
                rlist.remove(i)
                break
            print('receive client message:',data.decode())
            i.send('receive client message'.encode())

s.close()
