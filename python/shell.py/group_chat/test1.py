#!/usr/bin/python3

'''
pass :占位符，无任何操作。

continue: 跳出本次循环

break：结束本次循环

exit（）：结束整个程序
'''

#测试pass
num = 1
while num < 5:
    num +=1
    if num == 3:
        pass
        print(num)
    print(num)
print('test pass over')
#会打印   2,3,3,4,5,'test pass over'

#测试continue
num = 1
while num < 5:
    num +=1
    if num == 3:
        continue
        print(num)
    print(num)
print('test continue over')
#会打印   2,4,5,'test continue over'

#测试break
num = 1
while num < 5:
    num +=1
    if num == 3:
        break
        print(num)
    print(num)
print('test break over')
#会打印   2,'test break over'

#测试exit()
num = 1
while num < 5:
    num +=1
    if num == 3:
        exit()
        print(num)
    print(num)
print('test exit() over')
#会打印   2
