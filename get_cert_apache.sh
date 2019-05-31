#!/bin/sh

DOMAIN=hosname.domain.ru|com
IP=xternal ip_add (example 1.1.1.1)
PORT=external port (example 7777)
DIR=/etc/apache2/ssl/le

cd /tmp

(
  echo mget live/$DOMAIN/fullchain.pem
  echo mget live/$DOMAIN/privkey.pem
) | sftp -P$PORT le@$IP || exit 1

if [ -z $DIR/fullchain.pem -o -z $DIR/privkey.pem ] ; then
 echo "Empty certificate"
 exit 1
fi
diff -q fullchain.pem $DIR/fullchain.pem && exit 0

mkdir $DIR/old >/dev/null 2>&1
cp -p $DIR/fullchain.pem $DIR/privkey.pem $DIR/old/
mv fullchain.pem privkey.pem $DIR/

if ! `service apache2 restart >/dev/null 2>&1` ; then
 echo "Bad certificate"
 mv $DIR/old/* $DIR/
 service apache2 reload
 exit 1
fi
