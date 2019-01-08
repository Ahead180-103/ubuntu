#!/usr/bin/python3

from multiprocessing import Semaphore, Pool
import os
import time

semaphore = Semaphore(1)


def worker_process():
        print(id(semaphore))
        semaphore.release()
    #with semaphore:
        print("Process  pid : (%s) " % os.getpid()\
                ,'parents pid : (%s)' % os.getppid())
        time.sleep(3)
        #print("Process (%s) ended" % os.getpid())


if __name__ == '__main__':
    print(id(semaphore))
    pool = Pool(5)
    for i in range(0, 10):
        pool.apply_async(worker_process)
    pool.close()
    pool.join()
    print('main process pid : %s'% os.getpid())
    print("Main Process ended")
    print(semaphore.get_value())
    print(id(semaphore))
