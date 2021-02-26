from .BaseApp import BasePage
from selenium.webdriver.common.by import By

class GmailMainPageLocators:
    LOCATOR_NEW_MAIL_BUTTON = (By.XPATH, ".//*[text()='Написать']")
    LOCATOR_RECEPIEN_FIELD = (By.NAME, "to")
    LOCATOR_SUBJECT_FIELD = (By.NAME, "subjectbox")
    LOCATOR_MAIL_TEXT_FIELD = (By.XPATH, "(.//*[@aria-label='Тело письма'])[2]")
    LOCATOR_SEND_MAIL_BUTTON = (By.XPATH, ".//*[text()= 'Отправить']")
    LOCATOR_SUCCESS_SEND = (By.XPATH, ".//*[text()= 'Письмо отправлено.']")

class SendMail(BasePage):

    def count_mail(self,sender):
        count = len(self.find_elements((By.XPATH, f"(.//*[@class='afn']//*[@name='{sender}'])")))
        return count

    def click_new_email_button(self):
        button = self.find_element_to_be_clickable(GmailMainPageLocators.LOCATOR_NEW_MAIL_BUTTON)
        button.click()

    def enter_recepient(self, recepient):
        recepient_field = self.find_element(GmailMainPageLocators.LOCATOR_RECEPIEN_FIELD)
        recepient_field.send_keys(recepient)
    
    def enter_subject(self, subject):
        subject_field = self.find_element(GmailMainPageLocators.LOCATOR_SUBJECT_FIELD)
        subject_field.send_keys(subject)

    def enter_text_mail(self, text):
        text_field = self.find_element(GmailMainPageLocators.LOCATOR_MAIL_TEXT_FIELD)
        text_field.send_keys(text)

    def click_on_send_button(self):
        button = self.find_element_to_be_clickable(GmailMainPageLocators.LOCATOR_SEND_MAIL_BUTTON)
        button.click()

    def success_send_notification(self):
        self.find_element(GmailMainPageLocators.LOCATOR_SUCCESS_SEND)
