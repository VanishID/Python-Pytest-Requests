<h2>Автотесты на API проекта «Битва покемонов»</h2>

> **Статус проекта:**
> Проект закрытый для POST запросов, но GET можно выполнять без токена: https://pokemonbattle.ru/
> 
> 🟢 Поддерживается (активный) 

## Описание проекта и задачи
Автоматизировать часть проверок регресса с помощью Pytest и Requests

## Тест-кейсы, которые автоматизировали
* Проверить информацию о конкретном тренере и проверить, что пришел верный статус `GET /trainers`
* Проверить, что в ответе указано верное имя тренера `GET /trainers`
* Проверить, что в ответе пришел верный уровень тренера `GET /trainers`

 

Ожидаемый ответ: 
* response `status code` = 200
* в ответе в `json` приходит корректное поле `trainer_name`
* в ответе в `json` приходит корректное поле `level` 

## Детали реализации

1. Автотесты написаны с применением PyTest
2. Используется библиотека Requests

<img width="1917" height="759" alt="Image" src="https://github.com/user-attachments/assets/fa7f9630-2d4e-43c1-a498-1d6600fd3e65" />

## Локальный запуск тестов (из терминала)
1. Скачать проект
2. Перейти через терминал в директорию проекта
3. Выполнить команду:

Создаём виртуальное окружение внутри папки проекта.
Далее команды для MacOS (для windows инуструкция [есть вот тут](https://realpython.com/python-virtual-environments-a-primer/#create-it))

``` markdown
python3 -m venv venv
```

``` markdown
source venv/bin/activate
```

4. Устанавливаем библиотеки

``` markdown
python3 -m pip install requests
```

``` markdown
python3 -m pip install pytest
```

Запускаем
``` markdown
pytest tests/test_pokemon.py
```

5. Ожидаемый результат: получим отчет о прохождении тестов.


## Автор

Иван Депутатов ([Telegram](https://t.me/IvanD_QA), [Email](mailto:deputatovivan272@gmail.com))
