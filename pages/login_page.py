from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "E-mail input is not presented on login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PW), "Password input is not presented on login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BTN), "Submit button is not presented on login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Email input is not presented on registration form"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PW1), "Password input is not presented on registration form"
        assert self.is_element_present(*LoginPageLocators.REGISTER_PW2), "Confirm password input is not presented on registration form"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BTN), "Submit button is not presented on registration form"