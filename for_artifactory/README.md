### Тестирование проводилось на macOS Catalina version 10.15.6 в python 3.7, создавал виртуальную среду во избежание конфликтов с пакетами системы
```
Пример активации виртуальной среды: 

python3.7 -m venv scrapy_env
source scrapy_env/bin/activate
```
### После активации виртуальной среды, в терминале должен изменится ввод команд. Например:
```
(scrapy_env):~$ pip list
```
### Перед запуском скрипта необходимо добавить ваш токен от Artifactory в переменное окружение ОС
```
export TOKEN=ВАШ ТОКЕН

# проверка добавленных вами данных
echo $TOKEN
```
### Запуск скрипта
```
python3 search_snapshot_alternative.py
```

## TODO
1. переделать os.system(CURL) на requests

2. подумать как лучше параметризировать ARTIFACTORY_BASE_URL, ARTIFACTORY_COMMAND_URL, ARTIFACTORY_COMMAND_DIRECTORY_URL 

Возможно даже запрашивать при запуске 
