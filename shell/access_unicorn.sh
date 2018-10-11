#!/bin/bash
year=`date +%Y`
year_ago=`date -d "1 year ago" +%Y`
echo $year
echo $year_ago

month=`date +%m`
month_ago=`date -d "1 month ago"  +%m`
echo $month
echo $month_ago

day=`date +%d`
day_ago=`date -d "1 day ago" +%d`
echo $day
echo $day_ago

sed -i  "/^awk/s@\b${day_ago}\b@${day}@2"  /opt/access_analysis/access_unicorn.sh  &>/dev/null
sed -i  "/^awk/s@\b${month_ago}\b@${month}@1"  /opt/access_analysis/access_unicorn.sh  &>/dev/null
sed -i  "/^awk/s@\b${year_ago}\b@${year}@1"  /opt/access_analysis/access_unocorn.sh    &>/dev/null

datetime=`date`
echo $datetime >> /opt/access_analysis/unicorn_log/access-${year}-${month}-${day_ago}.txt

awk '/2018\/10\/10/{x[gensub(":.*","","1",$8)]++}END{for(i in x)if(x[i]>100&&i~"[0-9]"){print x[i],i}}' /mnt/g    o_server/unicorn9000/logs/temp_logs.log /mnt/go_server/unicorn9000/logs/2018*.log | sort -nr >>/opt/access_ana    lysis/unicorn_log/access-${year}-${month}-${day_ago}.txt
