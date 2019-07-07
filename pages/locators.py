from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators(object):
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#login_form input[name="login-username"]')
    LOGIN_PW = (By.CSS_SELECTOR, '#login_form input[name="login-password"]')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[name="login_submit"]')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#register_form input[name="registration-email"]')
    REGISTER_PW1 = (By.CSS_SELECTOR, '#register_form input[name="registration-password1"]')
    REGISTER_PW2 = (By.CSS_SELECTOR, '#register_form input[name="registration-password2"]')
    REGISTER_BTN = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators(object):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_color')
    PRICE_IN_CART = (By.CSS_SELECTOR, '.basket-mini')
