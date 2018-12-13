#!/usr/bin/python3
#_*_coding=utf-8 _*_

import sys
print("计算1/x的值")
while True:
  try:
    number = int(input("enter a number:"))
    if number == 0:
        sys.stderr.write("除以0 error\n")
    else:
        a = "1/%d = %s" % (number,1/number)
        sys.stdout.write(a+"\n")
  except ValueError:
      print("请输入正整数")
      exit()
