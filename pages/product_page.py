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

    def get_product_name(self):
        pname = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return pname.text

    def get_product_price(self):
        pprice = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return pprice.text

    def should_be_product_name(self, prod_name):
        assert prod_name == self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_NAME).text, "Error"

    def should_be_product_price(self, prod_price):
        assert prod_price == self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_PRICE).text, "Error"

    def should_be_add_button(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON), 'No such button'

    def should_be_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME), 'No such product'

    def should_be_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE), 'No such price'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be disappeared"

    def go_to_basket_page(self):
        basket_page = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        basket_page.click()
