#!/bin/bash
 
#ethn=$1
 
while :
do
 sleep 5 
  TX_eth0=$(cat /proc/net/dev | grep eth0 | sed 's/:/ /g' | awk '{print $10}')
  TX_lo=$(cat /proc/net/dev | grep lo | sed 's/:/ /g' | awk '{print $10}')
 sleep 1
  TX_eth00=$(cat /proc/net/dev | grep eth0 | sed 's/:/ /g' | awk '{print $10}')
  TX_loo=$(cat /proc/net/dev | grep lo | sed 's/:/ /g' | awk '{print $10}')
 TX_e=$[TX_eth00-TX_eth0]
 TX_e=`echo $TX_e | awk '{print $1/1048576}'`
# echo ${TX%%.*}AA
echo $TX_e
 TX_l=$[TX_loo-TX_lo]
 TX_l=`echo $TX_l | awk '{print $1/1048576}'`
#	echo ${TX_l%%.*}I
echo $TX_l
done
