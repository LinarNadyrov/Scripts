#!/bin/sh

server=1.1.1.1
from=/opt/glassfish4/glassfish/domains/domain1/logs/KIWI 
to=/opt/logs/pN/tacN/kiwi
login=logs-pN
speed=1M
lock_file=/run/logs_move.lock
max_lock=3600

suff=`date +%s`

flock -w $max_lock $lock_file -c echo || exit 1

for log in `ls $from/*.gz 2>/dev/null` ; do
 name=`basename $log .gz`.$suff.gz
 rsync --bwlimit $speed -e 'ssh -i /root/.ssh/id_rsa_logs' -a $log $login@$server:$to/$name && rm -f $log
done

