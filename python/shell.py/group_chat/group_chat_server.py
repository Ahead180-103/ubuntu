#!/usr/bin/python3



from socket import *
import os,sys

#HOST = sys.argv[1]
#PORT = int(sys.argv[2])
#ADDR = (HOST,PORT)
ADDR = ('0.0.0.0',8888)

def do_login(s,user,name,addr):
     if (name in user) or name == "管理员":
         s.sendto('该用户存在'.encode(),addr)
         return
     else:
         s.sendto(b'ok',addr)
         msg = "\n欢迎 %s 进入聊天室"% name
         #print(msg)
         user[name] = addr
         for i in user:
             #print('进入for')
             if i != name:
                 s.sendto(msg.encode(),user[i])
                 #user[name] = addr
                 #print(user)            

def do_message(s,user,name,message):
     if not message:
         break
     else:
         msg = "\n%-5s 说:%s" % (name,message)
         for i in user:
             if i != name:
                 s.sendto(msg.encode(),user[i])

def do_quit(s,user,name):
     del user[name]
     msg = '\n' + name + "离开了聊天室"
     for i in user:
         s.sendto(msg.encode(),user[i])

def do_child(s):
    user = {}
    while True:
        msg,addr = s.recvfrom(1024)
        msglist = msg.decode().split(' ')
     
        if msglist[0] == 'L':
             do_login(s,user,msglist[1],addr)
    
        elif msglist[0] == 'C':
             do_message(s,user,msglist[1],' '.join(msglist[2:]))
          
        elif msglist[0] == 'Q':
             do_quit(s,user,msglist[1])
                

def do_parent(s):
    while True:
        data = input('管理员发言:')
        msg = 'C ' + '管理员 ' +  data
        s.sendto(msg.encode(),('127.0.0.1',8888)) 

def main():
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)

    pid = os.fork()
    if pid < 0:
        sys.exit('创建进程失败')
    elif pid == 0:
        do_child(s)
    else:
        do_parent(s)


if __name__ == '__main__':
    main()
















