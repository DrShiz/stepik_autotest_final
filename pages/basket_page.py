from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_is_empty_message(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE).text.split('.')[0] == 'Your basket is empty', "Basket is empty message is not presented, but should be"

    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_NOT_EMPTY), "Basket is not empty."
