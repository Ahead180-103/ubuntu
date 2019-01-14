#!/bin/bash

s_ip=www.svnup.cn
s_path=/root/python/
d_path=/root/inotifytest/


ping -c3 -i0.3 -W3 ${s_ip} > /dev/null
if [ $? -eq 0 ];then
#    while inotifywait  -rqq ${s_path}
#    do
        rsync -az ${s_path}  ${d_path}
#    done
fi


