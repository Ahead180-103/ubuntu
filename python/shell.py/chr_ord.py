#!/usr/bin/python3

'''
'ABCD...Z'
'AaBbCc...Zz'
'''

s=''
s1=''
for i in range(65,65+26):
    s+=chr(i)
    s1+=chr(i)
    s1+=chr(i+32)
print(s)
print(s1)
