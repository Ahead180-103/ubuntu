#!/usr/bin/python3

w=int(input("please enter:"))
j=1
while j<=w:
    line=" "*(w-j)+"*"*(j)
    j+=1
    print(line)
'''
   *
  **
 ***
****
'''

print()
j=w
while True:
    line=" "*(w-j)+"*"*(j)
    j-=1
    print(line)
    if j==0:
        break
'''
****
 ***
  **
   *
'''


print()
j=w
while True:
    line="*"*(j)+" "*(w-j)
    j-=1
    print(line)
    if j==0:
        break
'''
****
***
**
*
'''
print()
j=1
while j<=w:
    line="*"*(j)+" "*(w-j)
    j+=1
    print(line)
'''
*
**
***
****
'''





