# -*- coding: utf-8 -*-
#!/usr/bin/python

import redis
from os.path import abspath
import sys

# Номер ограничения
limiter = 20
# Подключение к Redis
redis_client = redis.Redis(host = '127.0.0.1', port = 6379)

# Ключ cmd-lenq должен содержать команду для запуска этой программы.
PATH_SCRIPTS = abspath(__file__)
one_key = 'cmd-lenq'
redis_client.set(one_key,PATH_SCRIPTS)
#print('result for ', one_key, '= ', redis_client.get(one_key))

# Принимаем в качестве первого аргумента значение $key
key = sys.argv[1]
for line in sys.stdin:
    if line.strip('\n') == "exit":
        break
    else:
        # Вносим данные в список, данные поступают с stdin
        redis_client.rpush(key, line.strip('\n'))
        # Содержимое списка должно быть ограничено 20 наиболее "свежими" элементами
        # Проверяем длину списка и соблюдаем ограничение в 20 наиболее "свежих" элементов
        # Вытесняем самый старый элемент, т.е первый
        redis_client.ltrim(key, -limiter, -1)

# запуск - python3 /home/user/python_work6-1.py 61