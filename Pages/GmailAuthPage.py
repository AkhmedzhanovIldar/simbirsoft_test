from .BaseApp import BasePage
from selenium.webdriver.common.by import By

class GmailAuthPageLocators:
    LOCATOR_EMAIL_FIELD = (By.ID, "identifierId")
    LOCATOR_EMAIL_NEXT_BUTTON = (By.ID, "identifierNext")
    LOCATOR_PASSWORD_FIELD = (By.NAME, "password")
    LOCATOR_PASSWORD_NEXT_BUTTON = (By.ID, "passwordNext")

class Auth(BasePage):

    def enter_login(self, email):
        login_field = self.find_element_to_be_clickable(GmailAuthPageLocators.LOCATOR_EMAIL_FIELD)
        login_field.click()
        login_field.send_keys(email)

    def click_on_email_next_button(self):
        button = self.find_element_to_be_clickable(GmailAuthPageLocators.LOCATOR_EMAIL_NEXT_BUTTON)
        button.click()

    def enter_password(self, password):
        password_field = self.find_element_to_be_clickable(GmailAuthPageLocators.LOCATOR_PASSWORD_FIELD)
        password_field.click()
        password_field.send_keys(password)

    def click_on_password_next_button(self):
        self.find_element_to_be_clickable(GmailAuthPageLocators.LOCATOR_PASSWORD_NEXT_BUTTON).click()

    def check_title(self, email):
        self.title_contains(email)