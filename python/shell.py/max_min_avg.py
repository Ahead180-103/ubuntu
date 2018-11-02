#!/usr/bin/python3

l=[]
while True:
   a=input('请输入数字: ')
   if a=="exit" or a=="quit" or a=="e" or a=="q":
      break
   l.append(int(a))
print(l)
print(max(l))
print(min(l))
s=sum(l)/len(l)
print(s)
