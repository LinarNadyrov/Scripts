#!/bin/bash

DUMP_STORAGE=p1-nfs

/usr/sbin/pct stop --skiplock 1 306
vzdump 306 -compress gzip -storage=$DUMP_STORAGE --maxfiles 3 -mode stop --mailto admin@vip-connect.ru --mailnotification always
/usr/sbin/pct start 306

