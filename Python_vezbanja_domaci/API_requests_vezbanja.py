# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "6"
# ///
# 1. Написати функцију get_user(user_id: int) -> dict која са JSONPlaceholder-а
# (https://jsonplaceholder.typicode.com/users/<user_id>) преузима корисника и враћа само
# име, email и град.
# Input: get_user(1)
# Output: {'name': 'Leanne Graham', 'email': 'Sincere@april.biz', 'city':
# 'Gwenborough'}
# Помоћ: град је унутар address
import requests

def get_user(user_id: int) -> dict:
    base_url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(f'{base_url}/users/{user_id}')
    data = user.json()
    return {
        'name': data['name'],
        'email': data['email'],
        'city': data['address']['city']
    }
print(get_user(1))

# COMMAND ----------

# 2. Написати функцију get_post_titles(user_id: int) -> list која враћа листу наслова свих постова једног корисника. Користити params={'userId': user_id}, а не филтрирање у Python-у.
# Input: get_post_titles(1)
# Output: листа од 10 наслова, први је 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit
def get_post_titles(user_id: int) -> list:
    lista = []
    base_url = 'https://jsonplaceholder.typicode.com'
    posts = requests.get(f'{base_url}/posts', params={'userId': user_id})
    data = posts.json()
    for post in data:
        lista.append(post['title'])
    return lista
print(get_post_titles(1))

# COMMAND ----------

# 3. Написати функцију get_current_temperature(latitude: float, longitude: float) -> float која преко Open-Meteo API-ја (https://api.open-meteo.com/v1/forecast, параметар current='temperature_2m') враћа тренутну температуру.
# Input: get_current_temperature(45.25, 19.84)
# Output: број (зависи од тренутне температуре)
# Помоћ: прво испишите цео одговор и пронађите где је температура
from pprint import pprint

def get_current_temperature(latitude: float, longitude: float) -> float:
    params = {
        'latitude': latitude,
        'longitude': longitude,
        'current': 'temperature_2m'  
    }
    data = requests.get('https://api.open-meteo.com/v1/forecast', params=params).json()
    pprint(data)

get_current_temperature(45.25, 19.84)

# COMMAND ----------

# 4. Написати функцију city_coordinates(city: str) -> tuple која преко Open-Meteo geocoding API-ја (https://geocoding-api.open-meteo.com/v1/search) враћа (latitude, longitude) првог резултата у Србији (countryCode='RS'). Ако град не постоји, подићи ValueError.
# Input1: city_coordinates('Novi Sad')
# Output1: око (45.25, 19.84)
# Input2: city_coordinates('Xyzzyville')
# Output2: ValueError: City not found: Xyzzyville
import requests

def city_coordinates(city: str) -> tuple:
    url = 'https://geocoding-api.open-meteo.com/v1/search'
    data = requests.get(url, params={'name': city, 'countryCode': 'RS', 'count':1}).json()     
    if 'results' not in data:
        raise ValueError(f'City not found: {city}')
    first = data['results'][0]
    return (first['latitude'], first['longitude'])

# print(city_coordinates('Novi Sad'))
print(city_coordinates('Xyzzyville'))