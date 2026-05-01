import requests                                                               # необходимые модули (импорт) для работы
import json

host="https://api.pokemonbattle.ru/v2"

pokemon_create = {                                                            # переменная тела запроса для создания покемона, значение-словарь
    "name": "generate",
    "photo_id":1
}

pokemon_knockout = {                                                          # переменная тела запроса для отправки покемона в нокаут
    "pokemon_id": "1355077"
}

pokemon_addpokeball= {
    "pokemon_id": "1241"                                                       # переменная тела запроса для поимки покемона в покебол
}

header= {'Content-Type': 'application/json', 'trainer_token': "490b847fe8d7497d8c5f9eed166f203d"}

trainer_id=57710                                                                                        # переменная, которой присвоено целое число

response_get = requests.get (url=f"{host}/trainers/{trainer_id}")                                      # получение инфо. о конкретном тренере

print (json.dumps(response_get.json(), indent=2, ensure_ascii=False))                                  # красиво оформленный ответ в формате Json с отображ. кирилл.


response_post = requests.post (url=f"{host}/pokemons", headers=header, json=pokemon_create)            # создание покемона

print (json.dumps(response_post.json(), indent=2, ensure_ascii=False)) 

response_get = requests.get (url=f"{host}/pokemons", params={"trainer_id":57710, "status":1})          # get запрос с указанием 2 квери параметров 

print (json.dumps(response_get.json(), indent=2, ensure_ascii=False)) 

response_post = requests.post (url=f"{host}/pokemons/knockout", headers=header, json=pokemon_knockout)  # отправить покемона в нокаут

print (json.dumps(response_post.json(), indent=2, ensure_ascii=False)) 