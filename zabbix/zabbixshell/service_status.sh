#!/bin/bash
case $1 in
mysql)
#ps -ef | grep "mysqld" | grep -v grep  | wc -l;;
ps -C  mysqld | wc -l;;
mongod)
#ps -ef | grep "mongod" | grep -v grep  | wc -l;;
ps -C  mongod | wc -l;;
redis)
#ps -ef | grep "redis_server" | grep -v grep  | wc -l;;
ps -C  redis-server | wc -l;;
unicorn)
#ps -ef | egrep "unicorn.linux" | grep -v grep  | wc -l;;
ps -C unicorn.linux | wc -l;;
titan)
#ps -ef | egrep "titan.linux" | grep -v grep  | wc -l;;
ps -C titan.linux | wc -l;;
puff)
#ps -ef | egrep "puff.linux" | grep -v grep  | wc -l;;
ps -C puff.linux | wc -l;;
nginx)
#ps -ef | grep "nginx" | grep -v grep  | wc -l;;
ps -ef | awk '/nginx\:/{x++}END{print x}';;
esac
