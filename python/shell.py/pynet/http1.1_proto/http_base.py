
from socket import *


def headerClient(connfd):
    request = connfd.recv(4096).decode()
    #print('connection from %s' % connfd.getpeername())
    print(request)
    response = 'HTTP/1.1 200 ok'
    response += ''
    response += '\r\n'
    f = open('baidu.html',encoding='utf-8')
    data = f.read()
    response += data
    f.close()
    connfd.send(response.encode())


def tcpConnection():
    s = socket()
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    PORT = 9000
    s.bind(('0.0.0.0',PORT))
    s.listen(5)
    while True:
        print('listen port %s' % PORT)
        connfd,addr = s.accept()
        print('waiting client connection from:', addr)
        print(connfd)
        headerClient(connfd)

if __name__ == "__main__":
    tcpConnection()