#!/bin/bash
case $1 in
insert)
echo "db.serverStatus().opcounters" |/mnt/mongodb/bin/mongo  -uzabbix -p1  admin --quiet   | awk -F[,:]  '/insert/{print $2}';;
query)
echo "db.serverStatus().opcounters" |/mnt/mongodb/bin/mongo  -uzabbix -p1  admin --quiet   | awk -F[,:]  '/query/{print $2}';;
update)
echo "db.serverStatus().opcounters" |/mnt/mongodb/bin/mongo  -uzabbix -p1  admin --quiet   | awk -F[,:]  '/update/{print $2}';;
delete)
echo "db.serverStatus().opcounters" |/mnt/mongodb/bin/mongo  -uzabbix -p1  admin --quiet   | awk -F[,:]  '/delete/{print $2}';;
connection)
echo "db.serverStatus().connections" |/mnt/mongodb/bin/mongo  -uzabbix -p1  admin --quiet   | awk -F[,:]  '/current/{print $2}';;
esac
