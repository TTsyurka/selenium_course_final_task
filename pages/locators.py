from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.PARTIAL_LINK_TEXT, "basket")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL =(By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class ProductPageLocators():
    PRODUCT_NAME = (By.XPATH, "//article/div[1]/div[2]/h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    PRODUCT_NAME_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_PRICE_IN_BASKET = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_PRICE_NOTIFICATION = (By.CSS_SELECTOR, ".basket-items")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
