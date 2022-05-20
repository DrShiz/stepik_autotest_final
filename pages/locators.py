from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//*[@id='default']/header/div[1]/div/div[2]/span/a")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form1")
    REGISTER_FORM = (By.ID, "register_form1")

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    ORIGINAL_INFO = (By.CLASS_NAME, "product_main")
    BOOK_NAME_IN_BASKET = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    BOOK_PRICE_IN_BASKET = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasketPageLocators():
    BASKET_IS_EMPTY_MESSAGE = (By.ID, "content_inner")
    BASKET_IS_NOT_EMPTY = (By.CLASS_NAME, "basket-title")