from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_button()
        self.should_be_basket()

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()
    def should_be_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME), 'No such product'
    def should_be_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE), 'No such price'