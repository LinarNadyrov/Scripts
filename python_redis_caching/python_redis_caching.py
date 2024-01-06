# -*- coding: utf-8 -*-
#!/usr/bin/python

from sh import tail
import sys
import os
import redis
from os.path import abspath
from datetime import datetime
import argparse

# запуск - python3 python_work5.py -file /tmp/log_file_task5.log

# При запуске принимает в качестве аргумента путь к файлу 
parser = argparse.ArgumentParser(description="command line options",formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-file ', '--file_location', help="Source location")
args = parser.parse_args()
args_data = vars(args)

# Новый список
list_path = []
# Словарь забираем в список
for key, value in args_data.items():
    list_path.append(value)
text_file = list_path[0]

# Создаем файл и записываем/перезаписываем в него данные
text_data = [ '1string', '2string', '3string', '4string', '5string', '6string', '7string', '8string', '9string', '10string', '11string', '12string', '13string', '14string', '15string']
#text_file = '/tmp/log_file_task5.log'

with open(text_file, 'w', encoding='utf-8') as file:
    for line in text_data:
        file.write(line + '\n')

# Выводим в stdout 100 последних байт его содержимого
def tail_stdout(parametr_tail, path, _out=''):
    # Error in Python 3.8.10 = AttributeError: 'str' object has no attribute 'wait'
    try:
        p = tail(parametr_tail, path, _out=sys.stdout)
        p.wait()
    except:
        pass

# Записываем в файл 100 последних байт его содержимого
def tail_out(parametr_tail, path, _out=''):
    # Error in Python 3.8.10 = AttributeError: 'str' object has no attribute 'wait'
    try:
        p = tail(parametr_tail, path, _out=text_file_out)
        p.wait()
    except:
        pass

# Подключение к redis и проверка существование запрашиваемого ключа
# Скрипт читает файл только один раз, сколько бы не было вызовов с одинаковым аргументом.
lesson5_redis_key = 'testing_key'
lesson5_redis_data = 'script for lesson 5'
text_file_out = 'file_out.log'
redis_client = redis.Redis(host = '127.0.0.1', port = 6379)

if redis_client.exists(lesson5_redis_key) == 0:
    start_time = datetime.now()  # время начала выполнения
    #print('No date')
    tail_stdout('-c 100', text_file)
    redis_client.set(lesson5_redis_key,lesson5_redis_data)
    end_time = datetime.now()  # время окончания выполнения
    execution_time = end_time - start_time  # вычисляем время выполнения
    print(f'Program execution time: {execution_time} seconds')
else:
    start_time = datetime.now()  # время начала выполнения
    #print('Date',redis_client.exists(lesson5_redis_key))
    #tail_stdout('-c 100', text_file)

    print('result for ', lesson5_redis_key, '= ', redis_client.get(lesson5_redis_key))
    
    end_time = datetime.now()  # время окончания выполнения
    execution_time = end_time - start_time  # вычисляем время выполнения
    print(f'Program execution time: {execution_time} seconds')

# Ключ cmd-fcat должен содержать команду для запуска вашей программы 
PATH_SCRIPTS = abspath(__file__)
one_key = 'cmd-fcat'
redis_client.set(one_key,PATH_SCRIPTS)
print('result for ', one_key, '= ', redis_client.get(one_key))
