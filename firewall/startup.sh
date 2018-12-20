#!/bin/bash
#启动Nginx
sleep 0.5
nginx_status=`ps -C nginx | wc -l`
if [ $nginx_status -lt 2 ];then
   /data/nginx/sbin/nginx
   sleep 2
   nginx_status=`ps -C nginx | wc -l`
   [ $nginx_status -ne 1 ] && echo "nginx 已启动"
   [ $nginx_status -lt 2 ] && echo "nginx 启动失败"
else
   echo "nginx 是启动状态"
fi

#启动Mongodb
sleep 1
mongodb_status=`ps -C  mongod | wc -l`
if [ $mongodb_status -eq 1 ]; then
   /data/mongodb/bin/mongod  -f /data/mongodb/etc/mongodb.conf   &>/dev/null
   sleep 2
   mongodb_status=`ps -C mongod | wc -l`
   [ $mongodb_status -ne 1 ] && echo "mongodb 已启动"
   [ $mongodb_status -eq 1 ] && echo "mongodb 启动失败"
else
   echo "mongodb  是启动状态"
fi



#启动edm
sleep 1
edm_status=`ps -C edm.linux | wc -l`
if [ $edm_status -eq 1 ]; then
  cd /data/go_server/edm/
  nohup  ./edm.linux &  &>/dev/null
  sleep 2
  edm_status=`ps -C edm.linux | wc -l`
  [ $edm_status -ne 1 ] && echo "edm.linux  已启动"
  [ $edm_status -eq 1 ] && echo "edm.linux  启动失败"
else
   echo "edm.linxu 是启动状态"
fi



#启动factory
sleep 1
factory_status=`ps -C factory.linux | wc -l`
if [ $factory_status -eq 1 ];then
  cd /data/go_server/factory/
  nohup  ./factory.linux &   &>/dev/null
  sleep 2
  factory_status=`ps -C factory.linux | wc -l`
  [ $factory_status -ne 1 ] && echo "factory.linux  已启动"
  [ $factory_status -eq 1 ] && echo "factory.linux  启动失败"
else
  echo "factory.linux 是启动状态"
fi


#启动titan
sleep 1
titan_status=`ps -C titan.linux | wc -l`
if [ $titan_status -eq 1 ];then
  cd /data/go_server/titan/
  nohup  ./titan.linux &  &>/dev/null
  sleep 2
  titan_status=`ps -C titan.linux | wc -l`
  [ $titan_status -ne 1 ] && echo "titan.linux  已启动"
  [ $titan_status -eq 1 ] && echo "titan.linux  启动失败"
else
   echo "titan.linux 是启动状态"
fi


#启动unicorn
sleep 1
unicorn_status=`ps -C unicorn.linux | wc -l`
if [ $unicorn_status -eq 1 ];then
  cd /data/go_server/unicorn/
  nohup  ./unicorn.linux  &  &>/dev/null
  sleep 2
  unicorn_status=`ps -C unicorn.linux | wc -l`
  [ $unicorn_status -ne 1 ] && echo "unicorn.linux  已启动"
  [ $unicorn_status -eq 1 ] && echo "unicorn.linux  启动失败"
else
  echo "unicorn.linux 是启动状态"
fi







