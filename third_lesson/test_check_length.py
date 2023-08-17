# Ex10: Тест на короткую фразу

# python3 -m pytest -s test_check_length.py

class TestCheckLenght:
    def test_check_length(self):
        text = input('Введите текст: ')
        actual_lenght = len(text)
        excepted_lenght = 15
        assert actual_lenght < excepted_lenght, 'Длина строки больше 15 симовлов'