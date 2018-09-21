ps -eo %cpu,ucmd | awk '{a[$2]=+$1}END{for(i in a)if(a[i]>0){print i,a[i]}}' | head


ps -eo %cpu,ucmd | awk '{a[$2]=+$1}END{for(i in a)if(a[i]>0){print i,a[i]}}' | sort  -nr -k 2
