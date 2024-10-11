# -*- coding: utf-8 -*-
#!/usr/bin/python

import redis
from os.path import abspath
import sys
import random

# Подключение к Redis
redis_client = redis.Redis(host = '127.0.0.1', port = 6379, db=0)
# В качестве аргументов принимает имя ключа $key и число $number
key = sys.argv[1]
number = int(sys.argv[2])

# Функция, выполнения транзакции с помощью конвейера
def transaction(key,number):
    # Запуск конвейера (pipeline)
    pipe = redis_client.pipeline()
    # Очередь команд внутри транзакции
    pipe.multi()
    # Увеличение значения хранящееся в ключе на указанное число
    pipe.set(key, int(redis_client.get(key).decode("utf-8")) + number)
    # Выполнение транзакции
    pipe.execute()

# Проверяем существуют ли нужный наш ключ $key
if redis_client.exists(key) == 1:
    #print("Ключ существует")
    print("Ключ", key, "содержит значение:", redis_client.get(key).decode("utf-8"))
    transaction(key,number)
    print("Ключ", key, "значение после транзакции:", redis_client.get(key).decode("utf-8"))
else:
# Если нужного ключа нет, создаем его $key и докидываем случайное число
    redis_client.set(key,random.randint(1, 5))
    print("Ключ", key, "содержит значение:", redis_client.get(key).decode("utf-8"))
    transaction(key,number)
    print("Ключ", key, "значение после транзакции:", redis_client.get(key).decode("utf-8"))

# Команда на запуск должна лежать в ключе cmd-calc
PATH_SCRIPTS = abspath(__file__)
one_key = 'cmd-calc'
redis_client.set(one_key,PATH_SCRIPTS)
print("Ключ", one_key, 'содержит:', redis_client.get(one_key).decode("utf-8"))

# запуск - python3 /home/user/python_work8.py 81 14