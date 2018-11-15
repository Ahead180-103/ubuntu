#!/usr/bin/python3
#_*_coding=utf-8 _*_

import sys
print("计算1/x的值")
while True:
    number = int(input("enter a number:"))
    if number == 0:
        sys.stderr.write("除以0 error\n")
    else:
        a = "1/%d = %f" % (number,1/number)
        sys.stdout.write(a+"\n")
