import allure


# 1. Использование контекстного менеджера with allure.step(...)
def test_feature():
    with allure.step("Opening browser"):
        ...  # Тут код открытия браузера

    with allure.step("Creating course"):
        ...  # Тут код создания курса

    with allure.step("Closing browser"):
        ...  # Тут код закрытия браузера


# 2. Использование декоратора @allure.step
@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    pass


def test_featuret():
    create_course(title="Locust")
    create_course(title="Pytest")
    create_course(title="Python")
    create_course(title="Playwright")
