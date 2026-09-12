def test_user_login():
    assert 1 == 1


def test_first_try():
    print("Hello World!")


class TestUserAuthentication:
    def test_login(self):
        assert 1 == 1


def test_greeting():
    greeting = "Hello, world!"
    assert greeting == "Hi, world!"


def test_equal():
    assert 1 == 1


def test_not_equal():
    assert 1 != 2


def test_in_list():
    assert 3 in [1, 2, 3, 4]


def test_boolean():
    is_authenticated = True
    assert is_authenticated


def test_sum():
    assert 1 + 1 == 3, "Сумма 1 и 1 должна быть 2!"


def test_first_try():  # Этот тест мы добавили в предыдущем шаге
    print("Hello World!")


def test_assert_positive_case():  # Новый тест, которые проверяет положительный кейс
    assert (2 + 2) == 4  # Ожидается, что тест пройдет


def test_assert_negative_case():  # Новый тест, которые проверяет негативный кейс
    assert (2 + 2) == 5  # Тут должна быть ошибка
