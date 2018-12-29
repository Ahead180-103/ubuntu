

import os
from time import ctime,sleep

print(ctime())
pid = os.fork()

if pid < 0:
    print('create failed...')
elif pid == 0:
    sleep(2)
    print(pid)
    print('new create pid...')
else:
    sleep(1)
    print(pid)
    print('already exeist pid...')

print('close....')
print(ctime())
