from playwright.sync_api import sync_playwright, expect  # Импорт Playwright для синхронного проверки
# Домашнее задание

# Запуск Playwright в синхронном режиме
with sync_playwright() as playwright:
    # Открываем браузер Chromium (не в headless режиме, чтобы видеть действия)
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()  # Создаем новую страницу

    # Переходим на страницу авторизации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Находим поле "Email" и заполняем его
    email_input = page.locator('//div[@data-testid="registration-form-email-input"]//div//input')
    email_input.fill("user.name@gmail.com")

    # Находим поле "user_name" и заполняем его
    user_input = page.locator('//div[@data-testid="registration-form-username-input"]//div//input')
    user_input.fill("password")

    # Находим поле "password" и заполняем его
    password_input = page.locator('//div[@data-testid="registration-form-password-input"]//div//input')
    password_input.fill("password")

    # Кликаем кнопку регистрации
    registration_button = page.locator('//button[@data-testid="registration-page-registration-button"]')
    registration_button.click()

    dashboard_title = page.locator('//h6[@data-testid="dashboard-toolbar-title-text"]')
    expect(dashboard_title).to_be_visible()
    expect(dashboard_title).to_have_text('Dashboard')








#
#     # Находим кнопку "Login" и кликаем на нее
#     login_button = page.locator('//button[@data-testid="login-page-login-button"]')
#     login_button.click()
#
#     # Проверяем, что появилось сообщение об ошибке
#     wrong_email_or_password_alert = page.locator('//div[@data-testid="login-page-wrong-email-or'
#                                                  '-password-alert"]')
#     expect(wrong_email_or_password_alert).to_be_visible()  # Проверяем видимость элемента
#     expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")  # Проверяем текст
#
#     # Пауза на 5 секунд, чтобы увидеть результат
    page.wait_for_timeout(5000)