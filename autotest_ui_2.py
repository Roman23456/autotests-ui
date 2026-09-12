from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Проверяем, что кнопка Registration не активна
    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    #Заполним поле Email
    email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
    email_input.fill("user@mail.ru")

    # Зaполенение поля User
    user_input = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
    user_input.fill('Roman')

    # Заполнение поля Password
    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
    password_input.fill('12345')

    # Проверка что кнопка регистрации стала видимой
    registration_button_2 = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button_2).to_be_enabled()

    page.wait_for_timeout(5000)
