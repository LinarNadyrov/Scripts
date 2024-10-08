# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
import redis
from os.path import abspath

# Подключение к Redis
redis_client = redis.Redis(host = '127.0.0.1', port = 6379)

# Ключ cmd-ldeq должен содержать команду для запуска этой программы.
PATH_SCRIPTS = abspath(__file__)
one_key = 'cmd-ldeq'
redis_client.set(one_key,PATH_SCRIPTS)
#print('result for ', one_key, '= ', redis_client.get(one_key))

# Принимаем в качестве первого аргумента значение $key
key = sys.argv[1]
# Принимаем в качестве второго аргумента значение $limit
limit = sys.argv[2]

# Извлекаем $limit элементов из начала списка в ключе $key и выводим их в stdout
sys.stdout.write(str(redis_client.lpop(key, limit)))

# запуск - python3 /home/user/python_work6-2.py 61 5