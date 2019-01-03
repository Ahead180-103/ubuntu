#!/usr/bin/python3


from socket import *
import os,sys,signal


SERVER_ADDR = ('127.0.0.1',8888)


def do_child(s):
    while True:
         msg,addr = s.recvfrom(1024)
         print(msg.decode() + '\n发言(quit退出)',end='')
    

def do_parent(s,name,SERVER_ADDR):
    while True:
        data = input('发言(quit退出)')
        if data == 'quit':
            msg = 'Q ' + name
            s.sendto(msg.encode(),SERVER_ADDR)
            sys.exit('退出聊天室')
            os.kill(os.getppid(),signal.SIGKILL)
        else:
            msg = 'C ' + name + ' ' + data
            s.sendto(msg.encode(),SERVER_ADDR)
    



def main():
    s = socket(AF_INET,SOCK_DGRAM)
    while True:
        name = input('请输入姓名:')
        msg = 'L ' + name
        s.sendto(msg.encode(),SERVER_ADDR)

        msg,addr = s.recvfrom(1024)
        if msg.decode() == 'ok':
            print('@进入聊天室@')
            break

        else:
            print(msg.decode())

    pid = os.fork()

    if pid < 0:
        sys.exit('create failed exit')
    elif pid == 0:
        do_child(s)
    else:
         do_parent(s,name,SERVER_ADDR)
                     
#        msg,addr = s.recvfrom(1024)
#        print('receive server meeage:',msg.decode(),addr)
    
#    pid = os.fork()
#        
#    if pid < 0:
#        sys.exit('create failed exit')
#    elif pid == 0:
#        print('do_child success',os.getpid(),'ppid',os.getppid())
#        do_child(s)
#    else:
#        print('create perents success',os.getpid(),'child_pid',pid)
#        do_perents(s)


if __name__ == '__main__':
    main()
