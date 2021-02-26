import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Remote(command_executor="http://localhost:4445/wd/hub",
                              desired_capabilities={
                                  "browserName": "chrome",
                                  "platform": "WINDOWS",
                              })
    yield driver
    driver.quit()

