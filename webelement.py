from selenium.webdriver.common.by import By
from test import driver


class WebElement():

    def __init__(self, driver=driver, by = By):


        '''
        :param driver: webdriver is expected
        '''
        self.driver = driver
        self.by = By

    def create_web_element(self, locator):
        '''
        XPath is expected
        :param XPath locator:
        :return: webdriver find element
        '''
        return self.driver.find_element(self.by.XPATH, locator)

    def click(self):
        self.create_web_element().click()

    def fill_in(self, text):
        '''
        string is expected
        :param text:
        :return: create_web_element().send_keys(text)
        '''
        self.create_web_element().send_keys()