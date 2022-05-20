from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()
        # self.solve_quiz_and_get_code()

    def book_name_in_basket_is_correct(self):
        book_name = self.browser.find_element(*ProductPageLocators.ORIGINAL_INFO).text.split('\n')[0]
        book_name_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET).text

        assert book_name == book_name_in_basket, "Book name in basket is wrong"

    def book_price_in_basket_is_correct(self):
        book_price = self.browser.find_element(*ProductPageLocators.ORIGINAL_INFO).text.split('\n')[1]
        book_price_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_BASKET).text

        assert book_price == book_price_in_basket, "Book price in basket is wrong"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
