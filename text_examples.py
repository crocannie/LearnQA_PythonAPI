# Класс
class TestExample:
    # Функция
    def test_check_math(self):
        a = 5
        b = 9
        expected_summ = 14
        assert a + b == expected_summ, f"Сумма переменных а и б не равна {expected_summ}"

    def test_check_math2(self):
        a = 5
        b = 11
        expected_summ = 14
        assert a + b == expected_summ, f"Сумма переменных а и б не равна {expected_summ}"