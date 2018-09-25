#!/bin/bash
case $1 in
mysql)
ps -eo   %cpu,comm | awk '/mysqld/{x[$2]=+$1}END{for(i in x){print x[i]}}';;
mongod)
ps -eo   %cpu,comm | awk '/mongod/{x[$2]=+$1}END{for(i in x){print x[i]}}';;
redis)
ps -eo   %cpu,comm | awk '/redis-server/{x[$2]=+$1}END{for(i in x){print x[i]}}';;
nginx)
ps -eo   %cpu,comm | awk '/nginx/{x[$2]=+$1}END{for(i in x){print x[i]}}';;
unicorn)
ps -eo   %cpu,comm | awk '/unicorn\.linux/{x[$2]=+$1}END{for(i in x)if(i=="unicorn.linux"){print x[i]}}';;
titan)
ps -eo   %cpu,comm | awk '/titan\.linux/{x[$2]=+$1}END{for(i in x){print x[i]}}';;
puff)
ps -eo   %cpu,comm | awk '/puff\.linux/{x[$2]=+$1}END{for(i in x){print x[i]}}';;
unicorn_check)
ps -eo   %cpu,comm | awk '/unicorn\.linux_a/{x[$2]=+$1}END{for(i in x){print x[i]}}';;
esac
