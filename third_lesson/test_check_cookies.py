# Ex11: Тест запроса на метод cookie

# python3 -m pytest -s test_check_cookies.py

import requests

class TestCheckCookies:
    def test_check_cookies(self):
        url = 'https://playground.learnqa.ru/api/homework_cookie'
        response = requests.get(url=url)
        actual_cookie_value = response.cookies.get('HomeWork')
        excepted_cookied_value = 'hw_value'
        assert actual_cookie_value == excepted_cookied_value, f'Значение cookie HomeWork не соответствует {excepted_cookied_value}'
        


