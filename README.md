# Scripts
**file - get_cert_nginx.sh**
- Обновление ssl с помощью certbot
- Сервер на которым обновляем ssl НЕ ИМЕЕТ внешнего ip
---
**file - get_cert_apache.sh**
- Обновление ssl с помощью certbot
- Сервер на которым обновляем ssl НЕ ИМЕЕТ внешнего ip
---
**folder - nginx_bin**
- Обновление ssl с помощью certbot
- Сервер на которым обновляем ssl с внешним ip
---
**file - glassfish**
- Для запуска glassfish версии 4.1.1  (build 1)
- Данный файл подкладывается в /etc/init.d/glassfish 
---
**folder - windows**
- net_stop/start.bat - устраняет проблему с WmiPrvSE.exe | Выкл/Вкл службу "Инструментарий управления Windows"
- reboot.bat
---
**file - clear_crm.sh**
- обезличивание БД 
---
**folder - mount_in_kette**
- файл '/etc/rc.local' rc.local
- скрипт монтирования mount.sh 
- работает на Ubuntu 16.04.6 LTS 
----
**folder - lock_unlock_sql**
- lock.sql/unlock.sql - Блокировка/Разблокировка прикладных УЗ
- lockTA.sql/unlockTA.sql - Блокировка/Разблокировка отделенную УЗ
----
**file - search_mail.py**
- подключение к почтовому аккаунту по прокотолу IMAP
- поиск последнего письма по параметрам: \
(from_address = '(FROM "info@itbegin.ru")' \
(subject_head = '(SUBJECT "Help Desk")'
----
**folder - haproxy**
Основная суть:
- Балансировщик опрашивает backend с помощью zabbix-get и на основе нагруженности (CPU Load Average) распределяет подключения 
- проверено на Ubuntu 18.04.3 LTS
- проверено на Haproxy 2.0 
- необходимо установить на балансировщик - zabbix-get
- check_make_haproxy.pl - основной файл, логика обработки и построения модели балансировки  
- haproxy.cfg.template - template, основная логика после обработки, пишется сюда (файл скелет)
    template создает конфиг файл haproxy.cfg
- haproxy - cron файл 
----
**folder - backup**
 - file - do_306_backup.sh - Остановка lxc 306 & Бэкап
 - file - do_320_backup.sh - Остановка lxc 320 & Бэкап
 - file - copy_remote_backup_file.sh - Поиск файлов по дням изменения & Копирование данных файлов
 - file - copyp11p1 - Модифицированный & Поиск файлов по дням изменения & Копирование данных файлов
 - file - rename_weekly.sh - Перекладывание (mv) нужных файлов из одного каталога в другой
 - file - mv_weekly_backup.py - Поиск самого "старшего" файла и его перенос на другую директорию
 - file - mv_weekly.py - Перенос нужных файлов с одной на другую директорию
 ----
**folder - telegram**
 - file - telegram.sh - скрипт для отправки сообщений из zabbix. \
    Протестирован на Zabbix server 4.0.4 \
    Скрипт помещается /usr/lib/zabbix/alertscripts/ 
----
**folder - config_replica_pgsql9.2**
 - Конфиг файлы настройки репликации для PostgreSQL 9.2
----
**file - clear_data_in_cloud.sh**
- удаление файлов и папок в домашнем каталоге УЗ 
---
**folder - config_replica_pgsql10.5**
 - Конфиг файлы настройки репликации для PostgreSQL 10.5
---
**folder - for_artifactory**
 - Поиск и удаление определенных данных
---
**folder - check_ldap_and_keepalived**
 - Проверка порта на доступность и выполнение определенных действий
---
**folder - python_adapter_redis**
 - Redis адаптер на Python
---
**folder - python_redis_caching**
 - Кеширование данных с помощью Redis
---
**folder - python_redis_list**
 - Работа со списками в Redis
---
---
**folder - python_redis_transaction**
 - Работа с транзакциями (transaction) и pipeline в Redis
---
---
**folder - python_redis_pipeline**
 - Работа с pipeline в Redis
---
**folder - python_redis_brpop**
 - Работа с блокирующими режима команд в Redis
---
**folder - python_publish_subscribe**
 - Работа c подсистемами, реализующая абстракцию для отправки и получения уведомлений в Redis
---