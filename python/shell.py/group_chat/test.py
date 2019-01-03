#!/usr/bin/python3

#测试break
while True:
    name = input('请输入姓名:')
    if name == 'ok':
        print('@进入聊天室@')
        break

    else:
        print(name)

print('test break over')
