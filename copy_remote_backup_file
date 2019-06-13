#!/bin/sh

ip=external ip_add (example 1.1.1.1)
remote_path=/var/lib/vz/dump/
local_path=/rpool/w/dump

cd `dirname $0`

ssh rsync@$ip find $remote_path -name '*.tar.*' -cmin +60 -ctime -7 | sort -r |
 awk -vrp=$remote_path '{
  len=length(rp)+1+length("vzdump-lxc-xxx");
  if (substr($1,1,len)!=substr(last_name,1,len)) {
   print $1;
  }
  last_name=$1;
}' | awk -vip=$ip -vlocal_path=$local_path -vlp=$local_path '{ if (!system("rsync -ve \"ssh -lrsync\" -az "ip":/"$1" "lp"/")) system("./del_second_copy "local_path" "$1) }'

