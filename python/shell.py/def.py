#!/usr/bin/python3

def power(x,n):
  s=1
  while n>0:
      s=s*x
      n-=1
  return s

a=int(input('please enter: '))
b=int(input('please enter: '))
print(power(a,b))
