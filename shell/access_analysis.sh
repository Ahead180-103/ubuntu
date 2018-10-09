#!/bin/bash
year=`date +%Y`
echo $year

month=`date`
month=`echo $month | awk '{print $2}'`
echo $month

day=`date +%d`
echo $day

datetime=`date`
echo $datetime >> /opt/access_analysis/access.txt

awk '/09\/Oct\/2018/{x[$1]++}END{for(i in x)if(x[i]>100){print x[i],i}}' /var/log/nginx/access.log | sort -nr >> /opt/access_analysis/access.txt

awk '/09\/Oct\/2018/{x[$1]++}END{for(i in x)if(x[i]>100){print x[i],i}}' /var/log/nginx/access.log.1 | sort -nr >> /opt/access_analysis/access.txt
echo "" >> /opt/access_analysis/access.txt
echo ""  >> /opt/access_analysis/access.txt
