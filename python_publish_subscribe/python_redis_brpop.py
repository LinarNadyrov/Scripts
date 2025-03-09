import redis
import random
import sys

# Подключение к Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# Генерация случайного числа с тремя семёрками и чётными остальными цифрами
while True:
    n = random.randint(1000000000, 9999999999)  # 10-значное число
    s = str(n)
    if s.count('7') >= 3 and all(digit in '02468' for digit in s if digit != '7'):
        break

# Формирование строки s (количество каждой цифры)
count = [0] * 10
for digit in s:
    count[int(digit)] += 1
s_count = ''.join(map(str, count))

# Публикация или подписка
if len(sys.argv) < 2:
    print("Использование: python program.py <name> [--publish]")
    sys.exit(1)

name = sys.argv[1]
channel = f"{name}:{s_count}"

if "--publish" in sys.argv:
    # Публикация числа
    redis_client.publish(channel, n)
    print(f"Опубликовано число {n} в канал {channel}")
else:
    # Подписка на канал
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)
    print(f"Подписан на канал {channel}. Ожидание числа...")
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Получено число: {message['data'].decode()}")
            break

# 1. Запускаем программу для публикации числа:
# python python_work09.py work09_channel --publish
# Публикуем число, например, 7772468024, в канал work09_channel:0010203000.

# 2. В другом окне запускаем программу для подписки на канал:
# python python_work09.py work09_channel
# Она подпишется на канал work09_channel:0010203000 и выведет полученное число.
