ss -atn | awk '{print $5}' | awk '/[0-9]+.[0-9]+.[0-9]+.[0-9]+/{x[gensub(":.*","","g")]++}END{for(i in x)print x[i],i}' | sort -nr
