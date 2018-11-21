#!/usr/bin/python3
#_*_ conding=utf-8 _*_


##sys.agv 测试

import sys
VERSION="1.0"

def help(argv0):
    print("use may:")
    print("cmdline[-h -v]")
    print("-h  show help info\
         \n-v  show version info")
    return
def  version():
     print("comdline version is:", VERSION)
     return
def main():
    i=0
    for argv in sys.argv:
        if argv == "-v":
               version()
        elif argv == "-h":
               help(sys.argv[0])
main()
