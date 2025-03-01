# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
import redis
from os.path import abspath

def wait_for_items(count, keys):
    # Подключаемся к Redis
    r = redis.Redis(host='localhost', port=6379, db=0)

    # Команда на запуск должна лежать в ключе cmd-wait
    PATH_SCRIPTS = abspath(__file__)
    one_key = 'cmd-wait'
    r.set(one_key, PATH_SCRIPTS)
    print("Ключ", one_key, 'содержит:', r.get(one_key).decode("utf-8"))

    # Словарь для хранения значений по ключам
    items = {key: [] for key in keys}

    # Ожидаем значения из списков в Redis
    while True:
        # Используем BRPOP для блокирующего ожидания данных
        # BRPOP возвращает пару (ключ, значение) или None, если время ожидания истекло
        result = r.brpop(keys, timeout=5)

        if result is None:
            # Если время ожидания истекло, завершаем программу с ошибкой
            print("Timeout: не удалось получить все значения за 5 секунд", file=sys.stderr)
            sys.exit(1)

        # Извлекаем ключ и значение
        key, item = result
        key = key.decode('utf-8')
        item = item.decode('utf-8')

        # Добавляем значение в словарь
        items[key].append(item)

        # Проверяем, набрали ли мы нужное количество значений для этого ключа
        if len(items[key]) == count:
            # Если набрали, выводим все значения
            for k in keys:
                for i in items[k]:
                    print(f"{k} {i}")
            return

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Использование: python script.py <count> <key1> <key2> ...", file=sys.stderr)
        sys.exit(1)

    count = int(sys.argv[1])
    keys = sys.argv[2:]

    wait_for_items(count, keys)

# Добавляем данные в Redis (например, с помощью lpush):
# redis-cli lpush key1 value1
# redis-cli lpush key2 value2
# redis-cli lpush key3 value3
#
# Запуск - python3 /home/user/python_work10.py 3 key1 key2 key3
# в другом окно подключенный к Redis запускаем:
# lpush key3 value4
# lpush key3 value5
# lpush key3 value6
#
# Видим, что обрабатывает