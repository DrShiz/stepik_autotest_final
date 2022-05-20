from selenium.webdriver.common.by import By


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