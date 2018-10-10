#!/bin/bash
year=`date +%Y`
echo $year
year_ago=`date -d "1 year ago" +%Y`
echo ${year_ago}

month=`date +%h`
echo $month
month_ago=`date -d "1 month ago"  +%b`
echo ${month_ago}

day=`date +%d`
echo $day
day_ago=`date -d "1 day ago" +%d`
echo ${day_ago}

sed -i  "/^awk/s@\b${day_ago}\b@${day}@g"  /root/access_analysis.sh  &>/dev/null
sed -i  "/^awk/s@\b${month_ago}\b@${month}@g"  /root/access_analysis.sh  &>/dev/null
sed -i  "/^awk/s@\b${year_ago}\b@${year}@g"  /root/access_analysis.sh    &>/dev/null


datetime=`date`
echo $datetime >> /opt/access_analysis/access`date +%y%m%d-%H%M`.txt

awk '/10\/Oct\/2018/{x[$1]++}END{for(i in x)if(x[i]>0){print x[i],i}}' /var/log/nginx/access.log | sort -nr >> /opt/access_analysis/access`date +%y%m%d-%H%M`.txt

awk '/10\/Oct\/2018/{x[$1]++}END{for(i in x)if(x[i]>0){print x[i],i}}' /var/log/nginx/access.log.1 | sort -nr >> /opt/access_analysis/access`date +%y%m%d-%H%M`.txt
echo "" >> /opt/access_analysis/access`date +%y%m%d-%H%M`.txt
echo ""  >> /opt/access_analysis/access`date +%y%m%d-%H%M`.txt
