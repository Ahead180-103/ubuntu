#!/usr/bin/python3


'''
输入三句话让左边空出20个空格
如;
            hello world
                    abc
                      a
'''

a=input('enter ha:' )
b=input('enter ha:' )
c=input('enter ha:' )
print("%20s" % a)
print("%20s" % b)
print("%20s" % c)


a=int(input("enter number: "))
print("%d%%" % a)




'''
以最长的字符长度算
'''
a=input('enter ha:' )
b=input('enter ha:' )
c=input('enter ha:' )
num=max(int(len(a)),int(len(b)),int(len(c)))
print(num)
print(" " * (num - len(a)) + a)
print(" " * (num - len(b)) + b)
print(" " * (num - len(c)) + c)



fmt="%%%ds" % num
print("fmt = ",fmt)
print(fmt % a)
print(fmt % b)
print(fmt % c)









