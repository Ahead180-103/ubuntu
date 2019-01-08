#!/usr/bin/python3

from multiprocessing import Process,Semaphore
from signal import *
import time
import os


print('start time:',time.ctime())
alarm(5)

def headler(sig,frame):
    if sig == SIGALRM:
         print('waiting SIGALRM....')
    elif sig == SIGINT:
         print('waiting CTRL + C....')

signal(SIGALRM,headler)
signal(SIGINT,headler)

while True:
    time.sleep(1)
    print('丁丁 Yolanda  I love you....')

