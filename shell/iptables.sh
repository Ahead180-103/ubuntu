#!/bin/bash


s=`awk '{if($1>=5000){print $2}}' ./aa.txt | wc -l`
a=`awk '{if($1>=5000){print $2}}' ./aa.txt`

if [ $s -ne 0 ];then
 for i in $a; do iptables -A INPUT -s $i -p tcp  -j DROP; done  
fi
