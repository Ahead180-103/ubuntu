
#f = open('test.txt',encoding='utf-8')
f = open('test.txt','rb')
data = f.read()
print(data.decode())
f.close()

