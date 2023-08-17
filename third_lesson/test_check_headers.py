# Ex12: Тест запроса на метод header

# python3 -m pytest -s test_check_headers.py

import requests

class TestCheckHeaders:
    def test_check_headers(self):
        url = 'https://playground.learnqa.ru/api/homework_header'
        response = requests.get(url=url)

        actual_header_value = response.headers.get('x-secret-homework-header')
        excepted_header_value = 'Some secret value'
        
        assert actual_header_value == excepted_header_value, f'Значение header x-secret-homework-header не соответствует {excepted_header_value}'
        


