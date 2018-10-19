#!/bin/bash
#echo "Please enter a service name!"
case $1 in
unicorn.linux)
ps -C unicorn.linux  &> /dev/null
[ $? -ne 0 ]  &&  echo -e  "\033[31municorn.linux is not started\033[0m" && exit
s=`pgrep unicorn.linux`
kill -2 $s
sleep 1
ps -C unicorn.linux  &> /dev/null
[ $? -ne 0 ]  && echo -e "\033[32municorn.linux is closed\033[0m" ;;
titan.linux)
ps -C titan.linux  &> /dev/null
[ $? -ne 0 ]  &&  echo -e  "\033[31mtitan.linux is not started\033[0m" && exit
s=`pgrep titan.linux`
kill -2 $s
sleep 1
ps -C titan.linux  &> /dev/null
[ $? -ne 0 ]  && echo -e "\033[32mtitan.linux is closed\033[0m" ;;
zabbix_agentd)
ps -C zabbix_agentd  &> /dev/null
[ $? -ne 0 ]  &&  echo -e  "\033[31mzabbix_agentd is not started\033[0m" && exit
s=`pgrep zabbix_agentd`
kill -2 $s
sleep 1
ps -C zabbix_agentd  &> /dev/null
[ $? -ne 0 ]  && echo -e "\033[32mzabbix_agentd is closed\033[0m" ;;
*)
echo -e  "\033[31mPlease enter 'unicorn.linux'  or  'titan.linux'  or 'zabbix_agentd'\033[0m" ;;
esac
