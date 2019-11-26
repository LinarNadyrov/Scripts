#!/bin/bash

WEEKLY_DIR=/rpool/w/dump

cd /var/lib/vz/dump || exit 1

#vzdump-lxc-777-2016_07_30-00_59_01.tar.gz
#/var/lib/vz/dump/vzdump-lxc-555-2016_08_01-03_16_35.tar.gz

for n in 555 666 777 ; do
 fn=`ls vzdump-lxc-$n-*.tar.gz | awk '{fn=$1}END{print fn}'`
 log=`basename $fn .tar.gz`.log
 ext=${fn:6}
 mv $fn $WEEKLY_DIR/weekly$ext
 rm $log
 delete_mask=`ls weekly-lxc-$n-*.tar.gz 2>/dev/null`
 if [ "$delete_mask" != "" ] ; then
  find $delete_mask -mtime +12 -delete
 fi
done

