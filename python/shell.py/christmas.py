#!/usr/bin/python3


'''
输入： 3
  ×
 ×××
×××××
  ×
  ×
  ×
'''

h=int(input('请输入: '))
s=0
a=1
while s < 2 :
   if s ==0:
    s+=1
    for i in range(1,h+1):
      line=' ' * (h-i) + '*' * a + ' ' * (h-i)
      a+=2
      print(line)
   if s==1:
    s+=1
    for i in range(1,h+1):
      line1=' ' * (h-1) + '*'
      print(line1)
print('程序结束')
