#!/bin/bash

SAVE_MONTH=1
DUMP_STORAGE=p2-data-nfs
DUMP_DIR=/mnt/pve/p2-data-nfs/dump
TMP_DIR=/ssd/dump_tmp

suffix=$(($(date +%W)%2))
rm $DUMP_DIR/320_ssd_disk_$suffix*
rm  $DUMP_DIR/320_disk_$suffix*
suffix=$suffix-$(date +%Y_%m_%d-%H_%M_%S)

/usr/sbin/pct shutdown 320
if tar zcf $DUMP_DIR/320_ssd_disk_$suffix.tgz /ssd/320_disk && \
   tar zcf $DUMP_DIR/320_disk_$suffix.tgz /data/320_disk && \
   vzdump 320 -compress gzip -tmpdir=$TMP_DIR -storage=$DUMP_STORAGE --maxfiles 2 -mode snapshot
then
 echo backup 320 disks ok
else
 rm  $DUMP_DIR/320_ssd_disk_$suffix.tgz  $DUMP_DIR/320_disk_$suffix.tgz 
fi

/usr/sbin/pct start 320

