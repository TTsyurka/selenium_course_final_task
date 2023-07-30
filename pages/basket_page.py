from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRICE_NOTIFICATION), "Basket is not empty"

    def should_be_text_in_empty_basket(self):
        message_in_the_basket = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text
        assert message_in_the_basket == "Your basket is empty. Continue shopping", "wrong message"

    def should_be_items(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_PRICE_NOTIFICATION), "Basket IS empty"