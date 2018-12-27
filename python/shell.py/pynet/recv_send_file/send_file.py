
while True:
    from socket import *
    from time import sleep

    s = socket()
    s.connect(('127.0.0.1',8888))

    while True:
        data = input('enter your filename:')
    #    print(data.decode())
        if not data:
            break
        try:
            f = open(data, 'rb')
            data = f.read()
            s.send(data)
            f.close()
        except:
            print('no such file or directory')
            break

    s.close()