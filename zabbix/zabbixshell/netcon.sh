#!/bin/bash
case $1 in
estab)
#ss -atunp | grep nginx | grep -i "estab" | wc -l;;
ss -atn | awk '/ESTAB/{x++}END{print x}';;
listen)
#ss -atunp | grep nginx | grep -i "listen" | wc -l;;
ss -atn | awk '/LISTEN/{x++}END{print x}';;
total)
#ss -atunp | grep nginx |  wc -l;;
ss -atn | awk '/.*/{x++}END{print x}';;
other)
#ss -atunp | grep nginx | egrep -iv "(estab|listen)" | wc -l;;
ss -atn | awk '$1!~"(LISTEN|ESTAB)"{x++}END{print x}';;
esac
