#!/bin/bash
#logFile=/usr/lib/zabbix/alertscripts/log.txt # для теста без бота
token=' ' # нужно сгенерить  
chat="$1"
subj="$2"
message="$3"
URL="https://api.telegram.org/bot$token/sendMessage"
text=$subj" "$message
curl -s -X POST $URL -d chat_id=$chat -d text="$text" | grep -q '"ok":true,'

