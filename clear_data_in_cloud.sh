#!/bin/bash
DIR_PATH=/var/www/nextcloud/data

NAME_FILE_1="Nextcloud Community.jpeg"
NAME_FILE_2="Nextcloud Manual.pdf"
NAME_FILE_3="Nextcloud.mp4"
NAME_FILE_4="Nextcloud.png"

DOC_NAME_FILE_1="About.odt"
DOC_NAME_FILE_2="About.txt"
DOC_NAME_FILE_3="Nextcloud Flyer.pdf" 

PHOTO_NAME_FILE_1="Coast.jpg"
PHOTO_NAME_FILE_2="Hummingbird.jpg"
PHOTO_NAME_FILE_3="Nut.jpg"

DIR_NAME_1="Documents"
DIR_NAME_2="Photos"

# удаление файлов
find $DIR_PATH -type f -name $NAME_FILE_1 -delete
find $DIR_PATH -type f -name $NAME_FILE_2 -delete
find $DIR_PATH -type f -name $NAME_FILE_3 -delete
find $DIR_PATH -type f -name $NAME_FILE_4 -delete
find $DIR_PATH -type f -name $DOC_NAME_FILE_1 -delete
find $DIR_PATH -type f -name $DOC_NAME_FILE_2 -delete
find $DIR_PATH -type f -name $DOC_NAME_FILE_3 -delete
find $DIR_PATH -type f -name $PHOTO_NAME_FILE_1 -delete
find $DIR_PATH -type f -name $PHOTO_NAME_FILE_2 -delete
find $DIR_PATH -type f -name $PHOTO_NAME_FILE_3 -delete
# удаление папок
find $DIR_PATH -type d -name $DIR_NAME_1 -delete
find $DIR_PATH -type d -name $DIR_NAME_2 -delete