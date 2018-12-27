


from socket import *
from select import *
from time import sleep

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(5)

p = poll()
fdmap = {s.fileno():s}
p.register(s,POLLIN | POLLERR)

while True:
    print('listen port ....')
    events = p.poll()
    for fd,event in events:
        if fd is s.fileno():
            c,addr = fdmap[fd].accept()
            print('connection form :',addr)
            p.register(c,POLLIN)
            fdmap[c.fileno()] = c
        elif event & POLLIN:
            data = fdmap[fd].recv(4096)
            if not data:
                fdmap[fd].close()
                p.unregister(fd)
                break
            print('receive client message:',data.decode())
            fdmap[fd].send('receive client  message'.encode())

s.close()
