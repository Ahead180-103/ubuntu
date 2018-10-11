#!/bin/bash
while inotifywait -rqq /root/tar.gz/
do
rsync --delete -az  /root/tar.gz/  192.168.85.133:/root/tar.gz/
done 
