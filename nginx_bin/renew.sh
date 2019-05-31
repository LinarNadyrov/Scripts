#!/bin/bash

BROWSERDIR=/var/ssl/letsencrypt/
BASESSLDOMAIN=/var/ssl/cert

function dnsEqual()
{
 n1=`host $1 | grep 'has address' | awk '{print $NF; exit}'` 2>/dev/null
 n2=`host $2 | grep 'has address' | awk '{print $NF; exit}'` 2>/dev/null
# echo "1=$1, 2=$2, n=$n1, n2=$n2"
 test "$n1" = "$n2"
}

function renew()
{
 DOMAINNAME=$1
 if [ "$DOMAINNAME" = "" ] ; then
	 return
 fi
 WORKDIR=$BASESSLDOMAIN/$DOMAINNAME
 mkdir -p $WORKDIR
 if ! [ -f $WORKDIR/account.key ]; then
 	openssl genrsa 2048 > $WORKDIR/account.key
 fi
 
 san="DNS:$DOMAINNAME"
 dnsEqual $DOMAINNAME www.$DOMAINNAME && san="$san,DNS:www.$DOMAINNAME"
 if dnsEqual $DOMAINNAME mail.$DOMAINNAME ; then
  san="$san,DNS:mail.$DOMAINNAME"
 fi
 
 if ! [ -f $WORKDIR/domain.key ]; then
  openssl genrsa 2048 > $WORKDIR/domain.key
 fi
 openssl req -new -sha256 -key $WORKDIR/domain.key -subj "/" -reqexts SAN -config <(cat `dirname $0`/openssl.cnf <(printf "[SAN]\nsubjectAltName=$san")) > $WORKDIR/domain.csr
 
 python `dirname $0`/letsencrypt.py --account-key $WORKDIR/account.key --csr $WORKDIR/domain.csr --acme-dir $BROWSERDIR > $WORKDIR/domain.crt || exit 1
 wget -O - https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem > $WORKDIR/domainCA.crt
 cat $WORKDIR/domain.crt $WORKDIR/domainCA.crt > $WORKDIR/chained.pem
}

for domain in `ls /var/ssl/cert/ | grep '\.'` ; do
 renew $domain
# sleep 600
done
 
service nginx reload


