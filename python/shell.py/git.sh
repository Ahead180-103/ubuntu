#!/bin/bash

cd /opt/github/ubuntu/python/shell.py/
git add .
git commit  -m "add"
git push

echo ""
echo ""
echo ""
echo ""
sleep 1

cd /opt/gitlab/myubuntu/python/shell.py/
git add . 
git commit  -m "add"
git push
