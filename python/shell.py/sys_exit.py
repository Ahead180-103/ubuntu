#!/usr/bin/python3
#_*_ coding: utf-8 _*_

import sys

def exitfunc(value):
    print(value)
    sys.exit(0)

print("hello")


try:
    sys.exit(2)
except SystemExit  as value:
    exitfunc(value)

print("come?")
