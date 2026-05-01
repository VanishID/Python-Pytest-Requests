import requests
import pytest
import json

host="https://api.pokemonbattle.ru/v2"
trainer_id="id тренера"
expected_trainer_name="имя тренера"                                                           #ожидаемое имя в ответе
expected_level_trainer="уровень тренера"                                                      #ожидаемый уровень тренера


def test_get_info_trainer():
    response_get = requests.get (url=f"{host}/trainers/{trainer_id}")                         #Проверяем информацию о тренере и смотрим приходит ли верный статус
    assert response_get.status_code==200, "Unexpected status code, Wait for 200"              #сравниваем, что статус код=200, иначе пишем ошибку

def test_check_name_trainer():
    response_get = requests.get (url=f"{host}/trainers/{trainer_id}")  
    assert response_get.status_code==200, "Unexpected status code, Wait for 200"  
    data = response_get.json() 
    actual_name = data.get("trainer_name")
    assert actual_name == expected_trainer_name, "Wrong  Name"                                #Проверяем, что в ответе ожидаемое имя
  
def test_check_level_trainer():
    response_get = requests.get (url=f"{host}/trainers/{trainer_id}")  
    assert response_get.status_code==200, "Unexpected status code, Wait for 200"  
    data = response_get.json() 
    actual_level = data.get("level")
    assert actual_level == expected_level_trainer, "Wrong Level"                              #Проверяем, что в ответе ожидаемый уровень тренера
