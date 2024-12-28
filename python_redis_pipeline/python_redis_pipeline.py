# -*- coding: utf-8 -*-
#!/usr/bin/python

import os.path
import sys
import redis
from os.path import abspath

# Подключение к Redis
redis_client = redis.Redis(host = '127.0.0.1', port = 6379)
# Переключаем в режим pipeline - конвейерный режим для ускорения процесса
redis_pipeline = redis_client.pipeline()

# Команда на запуск должна лежать в ключе cmd-fimp
PATH_SCRIPTS = abspath(__file__)
print(PATH_SCRIPTS)
one_key = 'cmd-fimp'
redis_pipeline.set(one_key,PATH_SCRIPTS)

# Принимаем в качестве первого аргумента значение $base (путь к директории)
base = sys.argv[1]

# Ключ вида data:${file}, где $file — полный путь к файлу.
keys_manual = 'date:'
search_keys = keys_manual + '*'

# проверка существования ключа, если да, удаляем эти ключи
for key in redis_client.scan_iter(search_keys,100):
    # count provides a hint to Redis about the number of keys to
    # return per batch.
    redis_pipeline.delete(key)

for address, dirs, files in os.walk(base):
    for name in files:
        key = keys_manual + os.path.join(address, name)
        redis_pipeline.set(key,'')
        print('successful key creation:', key)
# Выполняем режим pipeline
redis_pipeline.execute()

# Напишите программу, которая с помощью команды KEYS ищет все ключи, начинающиеся на data: и выводит на каждой
#   строке данные вида $size $file.
#   - Первое значение вы получите с помощью команды STRLEN, а второе — просто отрезав префикс от ключа.
#   - Команда на запуск должна лежать в ключе cmd-fdir.

# Команда на запуск должна лежать в ключе cmd-fdir
PATH_SCRIPTS = abspath(__file__)
print(PATH_SCRIPTS)
two_key = 'cmd-fdir'
redis_client.set(two_key,PATH_SCRIPTS)

for key in redis_client.keys(search_keys):
    print('$size=',redis_client.strlen(key),'$file =',key.decode('utf-8').lstrip(keys_manual))

# запуск - python3 /home/user/python_work7.py /home/user