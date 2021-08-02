#!/bin/bash
LOCAL_PATH=/opt
SCRIPT_FILE=keepalived_start.py

(sleep 5 &&  python3 $LOCAL_PATH/$SCRIPT_FILE) &
(sleep 10 && python3 $LOCAL_PATH/$SCRIPT_FILE) &
(sleep 15 && python3 $LOCAL_PATH/$SCRIPT_FILE) &
(sleep 20 && python3 $LOCAL_PATH/$SCRIPT_FILE) &
(sleep 25 && python3 $LOCAL_PATH/$SCRIPT_FILE) &
(sleep 30 && python3 $LOCAL_PATH/$SCRIPT_FILE) &
(sleep 35 && python3 $LOCAL_PATH/$SCRIPT_FILE) &
(sleep 40 && python3 $LOCAL_PATH/$SCRIPT_FILE) &
(sleep 45 && python3 $LOCAL_PATH/$SCRIPT_FILE) &
(sleep 50 && python3 $LOCAL_PATH/$SCRIPT_FILE) &
(sleep 55 && python3 $LOCAL_PATH/$SCRIPT_FILE) &
(sleep 60 && python3 $LOCAL_PATH/$SCRIPT_FILE) &
