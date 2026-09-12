import re

from playwright.sync_api import Page

from components.authentication.registration_form_component import RegistrationFormComponent
from elements.button import Button
from elements.link import Link
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.registration_link = None
        self.registration_form = RegistrationFormComponent(page)

        self.login_link = Link(page, 'registration-page-login-link', 'Login')
        self.registration_button = Button(page, 'registration-page-registration-button', 'Registration')

    def click_registration_link(self):
        self.registration_link.click()
        # Добавили проверку
        self.check_current_url(re.compile(".*/#/auth/registration"))

    def click_registration_button(self):
        self.registration_button.click()

