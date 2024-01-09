# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import redis
from os.path import abspath
from datetime import datetime
import argparse
import sys

# запуск - python3 /home/user/python_work5.py /tmp/log_file_task5.log

redis_client = redis.Redis(host = '127.0.0.1', port = 6379)

# Ключ cmd-fcat должен содержать команду для запуска вашей программы 
PATH_SCRIPTS = abspath(__file__)
one_key = 'cmd-fcat'
redis_client.set(one_key,PATH_SCRIPTS)
#print('result for ', one_key, '= ', redis_client.get(one_key))

# При запуске принимаем в качестве аргумента путь к файлу
text_file = sys.argv[1]

# Определяем количество байтов в файле
def all_bytes_from_file(FILE, NUMBER_BYTE):
    # https://openwritings.net/pg/python/python-read-file-one-byte-time
    with open(FILE, 'rb') as file:
        byte = file.read(NUMBER_BYTE)         # Читаем файл c 1-го байта.
        count = 0 
        while byte:
            byte = file.read(1)               # Читаем следующий байт.
            count +=1                         # Суммируем количество байтов.
        return count

# Читаем файл с определенного байта и суммируем символы 
def red_sum_n_bytes(FILE, NUMBER_BYTE):
    with open(text_file, "rb") as file:
        byte = file.read(NUMBER_BYTE)         # Читаем файл с N-го байта.
        count = ''
        while byte:
            byte = file.read(1)               # Читаем следующий байт.
            byte_to_str = str(byte.decode())
            count = count + byte_to_str       # Суммируем количество символов.
        return count

from_this_byte = 100                          # Последние N байт файла

# Подключение к redis и проверка существование запрашиваемого ключа
# Скрипт читает файл только один раз, сколько бы не было вызовов с одинаковым аргументом.

# Если нет нужного ключа в Redis
if redis_client.exists(text_file) == 0:
    start_time = datetime.now()  # время начала выполнения
    #print('No date')
    
    number_of_byte = all_bytes_from_file(text_file,1)
    if number_of_byte == 100 or number_of_byte < 100:
        list_byte_symfol = red_sum_n_bytes(text_file,1)
        redis_client.set(text_file,list_byte_symfol)
    else:
        last_hundred_bytes = number_of_byte - from_this_byte
        list_byte_symfol = red_sum_n_bytes(text_file,last_hundred_bytes)
        redis_client.set(text_file,list_byte_symfol)

    print(list_byte_symfol)

    end_time = datetime.now()  # время окончания выполнения
    execution_time = end_time - start_time  # вычисляем время выполнения
    print(f'Program execution time: {execution_time} seconds')

# Если нужный ключ в Redis существует
elif redis_client.exists(text_file) == 1:
    start_time = datetime.now()  # время начала выполнения
    # Читаем нужный ключ и выходим данные в stdout
    key = redis_client.get(text_file)
    print(key.decode())
    
    end_time = datetime.now()  # время окончания выполнения
    execution_time = end_time - start_time  # вычисляем время выполнения
    print(f'Program execution time: {execution_time} seconds')
