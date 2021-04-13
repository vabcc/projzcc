from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, "It is not basket link"

    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket is not empty, but should be"

    def should_be_message_that_basket_is_empty(self, message):
        assert message in self.browser.find_element(*BasketPageLocators.EMPTY_TEXT).text, "Message that basket is empty does not find"