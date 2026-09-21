import allure
from playwright.sync_api import Page, Locator, expect
from ui_coverage_tool import ActionType, SelectorType

from tools.logger import get_logger  # Импортируем get_logger
from tools.ui_coverage import coverage_tracker

logger = get_logger("BASE_ELEMENT")  # Инициализируем logger


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:
        return "base element"

    def track_coverage(self, action_type: ActionType, **kwargs):
        selector = f'[data-testid="{self.locator.format(**kwargs)}"]'
        coverage_tracker.track_coverage(
            selector=selector,
            action_type=action_type,
            selector_type=SelectorType.CSS
        )

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        locator = self.locator.format(**kwargs)
        step = f'Getting locator with "data-testid={locator}" at index "{nth}"'

        with allure.step(step):
            logger.info(step)  # Добавили логирование
            return self.page.get_by_test_id(locator).nth(nth)

    def click(self, nth: int = 0, **kwargs):
        step = f'Clicking {self.type_of} "{self.name}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)  # Добавили логирование
            locator.click()
            self.track_coverage(ActionType.CLICK, **kwargs)

    def check_visible(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is visible'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)  # Добавили логирование
            expect(locator).to_be_visible()
            self.track_coverage(ActionType.VISIBLE, **kwargs)

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has text "{text}"'

        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)  # Добавили логирование
            expect(locator).to_have_text(text)
            self.track_coverage(ActionType.TEXT, **kwargs)

