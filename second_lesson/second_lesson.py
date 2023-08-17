from json.decoder import JSONDecodeError
import requests
import json
import time

# Задание №1
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(json_text)
key = "messages"
if key in obj:
    print(obj[key][1]['message'])
else:
    print(f"Ключа {key} в JSON нет")

# Задание № 2
url = 'https://playground.learnqa.ru/api/long_redirect'
response = requests.get(url=url, allow_redirects=True)
history = response.history
print(len(history))
print(history[-1].url)

# Задание № 3
url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'
methods = ['POST', 'GET', 'PUT', "DELETE"]

response_head = requests.head(url=url)
print(f'{response_head.status_code}, {response_head.text}, ')

for i in methods:
    response = requests.request(i, url=url)
    print(f'{i}: {response.status_code}, {response.text}, ')

for method_param in methods:
    url_with_param = url + '?method=' + method_param
    for method in methods:
        response_post = requests.request(method, url=url_with_param)
        if method != method_param:
            if 'success' in response_post.text:
                print('Нашлось! Методы разные, но результат успешный:')
                print(f'Параметр: {method_param}; Метод: {method}, {response_post.text}')
        if method == method_param:
            if 'Wrong method provided' in response_post.text:
                print('Нашлось! Методы совпадают, но результат :')
                print(f'Параметр: {method_param}; Метод: {method}, {response_post.text}')

# Задание № 4
def check():
    status_task = requests.get(url=url, params={"token": token})
    text = json.loads(status_task.text)
    return text
url = 'https://playground.learnqa.ru/ajax/api/longtime_job'
create_task = requests.get(url=url)
response_text =  json.loads(create_task.text)
token = response_text['token']
seconds = response_text['seconds']
print(response_text)
data = {
    'status': 'text',
    'result': 1
}
if check()['status'] == 'Job is NOT ready':
    print(check()['status'])
    time.sleep(seconds)
    check()
if check()['status'] == 'Job is ready':
    print(check()['status'])
    print(check()['result'])
    if 'result' in data:
        print('Поле result в наличии')

# Задание № 5
url_get_cookie = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
url_check_cookie = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'
passwords = ['1',
'password',
'password',
'123456',
'123456',
'123456',
'123456',
'123456',
'123456',
'123456',
'2',
'123456',
'123456',
'password',
'password',
'password',
'password',
'password',
'password',
'123456789',
'3',
'12345678',
'12345678',
'12345678',
'12345',
'12345678',
'12345',
'12345678',
'123456789',
'qwerty',
'4',
'qwerty',
'abc123',
'qwerty',
'12345678',
'qwerty',
'12345678',
'qwerty',
'12345678',
'password',
'5',
'abc123',
'qwerty',
'abc123',
'qwerty',
'12345',
'football',
'12345',
'12345',
'1234567',
'6',
'monkey',
'monkey',
'123456789',
'123456789',
'123456789',
'qwerty',
'123456789',
'111111',
'12345678',
'7',
'1234567',
'letmein',
'111111',
'1234',
'football',
'1234567890',
'letmein',
'1234567',
'12345',
'8',
'letmein',
'dragon',
'1234567',
'baseball',
'1234',
'1234567',
'1234567',
'sunshine',
'iloveyou',
'9',
'trustno1',
'111111',
'iloveyou',
'dragon',
'1234567',
'princess',
'football',
'qwerty',
'111111',
'10',
'dragon',
'baseball',
'adobe123',
'football',
'baseball',
'1234',
'iloveyou',
'iloveyou',
'123123',
'11',
'baseball',
'iloveyou',
'123123',
'1234567',
'welcome',
'login',
'admin',
'princess',
'abc123',
'12',
'111111',
'trustno1',
'admin',
'monkey',
'1234567890',
'welcome',
'welcome',
'admin',
'qwerty123',
'13',
'iloveyou',
'1234567',
'1234567890',
'letmein',
'abc123',
'solo',
'monkey',
'welcome',
'1q2w3e4r',
'14',
'master',
'sunshine',
'letmein',
'abc123',
'111111',
'abc123',
'login',
'666666',
'admin',
'15',
'sunshine',
'master',
'photoshop',
'111111',
'1qaz2wsx',
'admin',
'abc123',
'abc123',
'qwertyuiop',
'16',
'ashley',
'123123',
'1234',
'mustang',
'dragon',
'121212',
'starwars',
'football',
'654321',
'17',
'bailey',
'welcome',
'monkey',
'access',
'master',
'flower',
'123123',
'123123',
'555555',
'18',
'passw0rd',
'shadow',
'shadow',
'shadow',
'monkey',
'passw0rd',
'dragon',
'monkey',
'lovely',
'19',
'shadow',
'ashley',
'sunshine',
'master',
'letmein',
'dragon',
'passw0rd',
'654321',
'7777777',
'20',
'123123',
'football',
'12345',
'michael',
'login',
'sunshine',
'master',
'!@#$%^&*',
'welcome',
'21',
'654321',
'jesus',
'password1',
'superman',
'princess',
'master',
'hello',
'charlie',
'888888',
'22',
'superman',
'michael',
'princess',
'696969',
'qwertyuiop',
'hottie',
'freedom',
'aa123456',
'princess',
'23',
'qazwsx',
'ninja',
'azerty',
'123123']
unique_passwords = set(passwords)
for i in unique_passwords:
    response_get_cokkie = requests.post(url=url_get_cookie, data={'login': 'super_admin', 'password': i})
    auth_cookie = response_get_cokkie.cookies
    response_check_cookie = requests.get(url=url_check_cookie, cookies=auth_cookie)
    if response_check_cookie.text == 'You are authorized':
        print(f'{response_check_cookie.text}, {i}')

