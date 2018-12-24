
while True:
    data = input('enter string:')
    if not data:
        break
    f = open('write.txt','wb+')
    f.write(data.encode())

    print('start read...')

    f = open('write.txt','rb')
    data = f.read()
    print(data.decode())
f.close()

