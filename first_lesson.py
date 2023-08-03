
import requests
#Задание №1
name = 'Anna'
print(f'Hello, {name}!')

#Задание №2
url = 'https://playground.learnqa.ru/api/get_text'
response = requests.get(url)
print(response.text)