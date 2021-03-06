from selenium.webdriver.common.by import By


class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "xpath":
            return By.XPATH
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "id":
            return By.ID
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            print("Locator type {} not correct/supported".format(locatorType))
        return False

    def getElement(self, locator, locatorType="xpath"):
        element = None
        try:
            # locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
        except:
            print("Element not found with locator: {locator} and  locatorType: {locatorType}".format(
                locator=locator, locatorType=locatorType))
        return element

    def elementClick(self, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
        except:
            print("Cannot click on the element with locator: {locator} locatorType: {locatorType}".format(
                locator=locator, locatorType=locatorType))

    def sendKeys(self, data, locator, locatorType="xpath"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
        except:
            print("Cannot send data on the element with locator: {locator} locatorType: {locatorType}".format(
                locator=locator, locatorType=locatorType))

    def isElementPresent(self, locator, locatorType='xpath'):
        try:
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

































# from test import driver
# from selenium import webdriver
#
#
# class WebElement():
#     driver = webdriver.Chrome('driver/chromedriver')
#
#     def __init__(self, driver=driver):
#
#
#         '''
#         :param driver: webdriver is expected
#         '''
#         self.driver = driver
#
#     def create_web_element(self, locator):
#         '''
#         XPath is expected
#         :param XPath locator:
#         :return: webdriver find element
#         '''
#         return self.driver.find_element(self.by.XPATH, locator)
#
#     def click(self, element):
#         self.element.click()
#
#     def fill_in(self, text):
#         '''
#         string is expected
#         :param text:
#         :return: create_web_element().send_keys(text)
#         '''
#         self.create_web_element().send_keys()