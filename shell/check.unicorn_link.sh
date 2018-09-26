#!/bin/bash
ss -atunp | awk '/unicorn\.linux/{x[$6]++}END{for(i in x)print x[i],i}' | sort -nr  >> ./link.log
#ss -atunp | awk '/unicorn\.linux/{x[$6]++}END{for(i in x)if(i!~/(127.0.0.1:.*|47.89.240.236:.*|:::*)/)print x[i],i}' | sort -nr
