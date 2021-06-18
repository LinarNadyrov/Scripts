#!/usr/bin/python3
# coding: utf-8

import os
import json
import datetime
from datetime import datetime
import re

ARTIFACTORY_BASE_URL = 'https://domain.ru/artifactory/'
ARTIFACTORY_COMMAND_URL = 'command_url'
ARTIFACTORY_COMMAND_DIRECTORY_URL = '/project_name'
ARTIFACTORY_API_URL = 'api/storage/'
## Документация про метод File List - https://www.jfrog.com/confluence/display/JFROG/Artifactory+REST+API#ArtifactoryRESTAPI-FileList 
ARTIFACTORY_METOD = '?list&deep=1&listFolders=1'
ARTIFACTORY = ARTIFACTORY_BASE_URL + ARTIFACTORY_API_URL + ARTIFACTORY_COMMAND_URL + ARTIFACTORY_COMMAND_DIRECTORY_URL + ARTIFACTORY_METOD

## Регулярное выражение для поиска каталога "CATALOG_NAME"
PATTERN_SNAPSHOT = '\d*\.\d*\.\d*-CATALOG_NAME$'

FULL_DATE = datetime.now()
DATE = FULL_DATE.strftime('%X' + '-' + '%d' + '-' + '%m' + '-' + '%Y')
UPLOADED_FILE = 'unloading_data-' + DATE + '.json'

## Подключаемся к REST API Artifactory и выгружаем данные
os.environ['TOKEN'] = os.environ.get('TOKEN')       ## берем данные с переменного окружения ОС 
os.environ['ARTIFACTORY'] = ARTIFACTORY
os.environ['UPLOADED_FILE'] = UPLOADED_FILE
CURL = 'curl -H "X-JFrog-Art-Api:$TOKEN" -X GET $ARTIFACTORY > $UPLOADED_FILE'
os.system(CURL)

## Использование метода load для чтения json-файла как объекта и преобразуем json-объект в python-объект (словарь)
with open(UPLOADED_FILE, 'r', encoding='utf-8') as f_n:
    OBJ = json.load(f_n)

## Забираем нужные нам данные
JSON_ARRAY = OBJ['files']

## Сортируем по времени и дате - сортировка данных от самого раннего значения даты и времени к самому позднему 
JSON_ARRAY.sort(key = lambda x: datetime.strptime (x ['lastModified'],'%Y-%m-%dT%H:%M:%S.%fZ'), reverse=True)

## Ищем соответствие и применяем регулярное выражение
JSON_ARRAY = list(filter(lambda x: x['folder'] == True and re.search(PATTERN_SNAPSHOT, x['uri']), JSON_ARRAY)) 

## Основной кусок кода - логика
DIRS = {}
for f in JSON_ARRAY:
    e = f ['uri'].split('/') # разбиваем строку на части по '/'
    k = '/'.join(e [:-1])    # 'откусываем' последний элемент - SNAPSHOT
    if k not in DIRS:
        DIRS[k] = []
    DIRS[k].append(f)

print('Данные которые можно удалять:')
for k, l in DIRS.items(): # k - директория; l - SNAPSHOT и остальные данные
    p = l[10:]            # выводим данные с N-го элемента
    for value in p:
        print(ARTIFACTORY_BASE_URL + ARTIFACTORY_COMMAND_URL + ARTIFACTORY_COMMAND_DIRECTORY_URL + value['uri'])

# Удаляем ранее закаченный json файл
if os.path.isfile(UPLOADED_FILE) == True:
    os.remove(UPLOADED_FILE)