from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://gmail.com/"

    def find_element(self, locator, time = 10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_element_to_be_clickable(self, locator, time = 10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def title_contains(self, title, time = 10):
        return WebDriverWait(self.driver, time).until(EC.title_contains(title),
                                                      message=f"Title not contain {title}")
    def go_to_site(self):
        return self.driver.get(self.base_url)