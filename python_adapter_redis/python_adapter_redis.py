# -*- coding: utf-8 -*-
#!/usr/bin/python

import redis
import argparse
from os.path import abspath

# Запуск - python3 python.py lorem foo ipsum bar

# То есть, первый агрумент — префикс ключа, второй и последующие — любые, нужно сохранить их в разные ключи, 
# сформированные из префикса, счётчика (хранящегося в префиксе) и индекса аргумента. 
# Задача на формирование ключей, сохранение значений и попробовать инкремент.

parser = argparse.ArgumentParser(description="command line options",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("main_argument", help="Основной аргумент",type=str )
parser.add_argument("one_argument", help="Первый аргумент", type=str)
parser.add_argument("two_argument", help="Второй аргумент", type=str)
parser.add_argument("three_argument", help="Третий аргумент", type=str)
args = parser.parse_args()
redis_data = vars(args)

# Подключение к redis, но с доп настройками charset="utf-8", decode_responses=True - https://stackoverflow.com/questions/44026515/python-redis-keys-returns-list-of-bytes-objects-instead-of-strings
# вывод из bytes objects переводим в strings
redis_client = redis.Redis(host = '127.0.0.1', port = 6379, charset="utf-8", decode_responses=True)

# Запишите (любым способом) в ключ cmd-asvr команду для запуска вашей программы, 
# например, для php это можно сделать так: redis-cli SET cmd-asvr "php /path/to/script.php".
PATH_SCRIPTS = abspath(__file__)
#print(PATH_SCRIPTS)
one_key = 'cmd-asvr'
add_one_data = redis_client.set(one_key,PATH_SCRIPTS)
result_one_data = redis_client.get(one_key)
print('result for ', one_key, '= ', result_one_data)

# Новый список
list_redis = []
# Словарь забираем в список
for key, value in redis_data.items():
    list_redis.append(value)
#print(list_redis)

# Забираем первый элемент для ключа
main_argument = list_redis[0]
# Добавляем первый элемент в качестве ключа и значение N.
N = 15
add_lorem_data = redis_client.set(main_argument,N)
result_lorem = redis_client.get(main_argument)
print('result for ', main_argument, '= ', result_lorem)

# Добавление инкремента
add_incr = redis_client.incr(main_argument)
# Сходить узнать какое сейчас значение для lorem (первого ключа)
result_lorem = redis_client.get(main_argument)
print('result for INCR = ', result_lorem)

# Удаляем первый элемент
list_redis.pop(0)
#print(list_redis)

# Составляем полный ключ
count = 0
for i in list_redis:
    print('Ключ = ', main_argument + '-' + result_lorem + '-' + str(count) + ' значение ключа', i)
    redis_client.set(main_argument + '-' + result_lorem + '-' + str(count),i)
    count += 1
