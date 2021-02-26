from Pages.GmailAuthPage import Auth
from Pages.GmailMainPage import SendMail
import allure


@allure.feature("Auth")
def test_auth(browser):
    gmail_auth_page = Auth(browser)
    login = 'ivanivanovtest79'
    password = 'PasswordSecret123!'
    with allure.step("Переход на сай"):
        gmail_auth_page.go_to_site()
    with allure.step("Ввод логина"):
        gmail_auth_page.enter_login(login)
    with allure.step("Нажатие кнопки далее"):   
        gmail_auth_page.click_on_email_next_button()
    with allure.step("Ввод пароля"):
        gmail_auth_page.enter_password(password)
    with allure.step("Нажатие кнопки далее"):
        gmail_auth_page.click_on_password_next_button()
    with allure.step("Проверка входа аккаунт по заголовку страницы"):
        gmail_auth_page.check_title(login)

@allure.feature("Send mail")
def test_send_mail(browser):
    send_mail = SendMail(browser)
    with allure.step("Подсчет количества писем от адресата"):
        count_mail = send_mail.count_mail('farit.valiahmetov')
    with allure.step("Нажатие кнопки написать"):
        send_mail.click_new_email_button()
    with allure.step("Ввод почты получателя письма"):
        send_mail.enter_recepient('farit.valiahmetov@simbirsoft.com')
    with allure.step("Ввод темы письма"):
        send_mail.enter_subject('Тестовое задание. Ахмеджанов')
    with allure.step("Добавление количества писем в текст письма"):
        send_mail.enter_text_mail(count_mail)
    with allure.step("Нажатие кнопки отправить"):
        send_mail.click_on_send_button()
    with allure.step("Поиск уведомления об успешной отправки письма"):
        send_mail.success_send_notification()

    