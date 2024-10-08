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

#key = 'cmd-home-work6-2'
key = input("Введите первый аргумент значение $key: ")
limit = int(input("Введите второй аргумент значение $limit: "))
element = limit + 1

# Заполняем список данными
for i in range(element):
    #print(i, end=";")
    redis_client.rpush(key,i)

# Извлекаем $limit элементов из начала списка в ключе $key и выводим их в stdout
sys.stdout.write(str(redis_client.lrange(key,0, limit)))
