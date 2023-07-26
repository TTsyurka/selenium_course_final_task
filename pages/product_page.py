from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_card(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def product_name_is_correct(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        good_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name == good_in_basket, "no such good in basket"

    def product_price_is_correct(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price == price_in_basket, "price is wrong"
