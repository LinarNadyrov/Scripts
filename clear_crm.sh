#!/bin/bash
# Список логинов "избранных" пользователей
whiteListUsers='("manager","ivan.ivanov")'

# Формируем имя файла для сохранения транкейтов
fileDir=`echo 'SELECT @@secure_file_priv' | mysql --user=root -N` # @@secure_file_priv - переменная с конфиг файла MySQL 
sqlFile=toTrancate.sql # имя файла
truncSQL=$fileDir$sqlFile # путь к файлу

# Список таблиц, которые нельзя полностью очищать
sysTables='"email_addr_bean_rel","email_addresses","fields_meta_data","upgrade_history","config","user_preferences"'  # просто так нам нужно!!!

# sql запрос, собирающий все таблицы к очистке
trunc='SELECT CONCAT("TRUNCATE TABLE ",T.table_schema,".",T.TABLE_NAME,";") INTO OUTFILE "'$truncSQL'" FROM INFORMATION_SCHEMA.tables T WHERE T.table_type = "BASE TABLE" AND T.table_schema="pbcm"'
trunc=$trunc' and T.table_name not like "acl%"'        # не берем похожее на acl 
trunc=$trunc' and T.table_name not like "users%"'      # не берем похожее на users
trunc=$trunc' and T.table_name not in ('$sysTables');' # не берем $sysTables

# create file with tables for truncate
echo $trunc | mysql --user=root 

echo 'GO!'
echo '#'
echo 'go truncate tables...'
mysql < $truncSQL # выполняем запросы из файла truncSQL
rm -r $truncSQL # удаляем файл truncSQL
echo '...done!'
echo '#'
echo 'clearing users and emails..'
usersIds='(select id from pbcm.users where user_name in '$whiteListUsers')' # выбираем id избранных УЗ 

# удаляем лишние УЗ 
# удаляем все лишние email адреса 
mysql --user=root << QUERY 
use pbcm;
delete from users_cstm where id_c not in $usersIds;
delete from users where id not in (select t.id from $usersIds as t);
delete from users_signatures where user_id not in $usersIds;
delete from users_feeds where user_id not in $usersIds;
delete from users_password_link where username in $whiteListUsers;
truncate table users_last_import; 
delete from email_addr_bean_rel where bean_id not in $usersIds;
delete from email_addresses where id not in (select email_address_id from email_addr_bean_rel);
QUERY

echo '...done!'
echo '#'
echo 'clearing upload...'
for f in /var/www/crm/upload/*; do rm -rf "$f"; done # удаляем данные в каталоге 
echo '...done!'
echo '#'
echo 'ALL DONE! Test it :)'