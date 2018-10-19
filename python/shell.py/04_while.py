#!/usr/bin/python3

'''
1/1-1/3+1/5-1/7+.....+1/(2*n-1) 的和
n最大取：1000000
1）打印这个和
2）打印这个和乘以4的值
'''

n=int(input("please enter:"))
sum=0
if n<=1000000:
 i=1
 while i<=n:
    s=1/(2*i-1)
    if i%2==0:
      sum=sum-s
    else:
      sum=sum+s
    i+=1
 print(sum)
 print(sum*4)
else:
    print("number not in range")


