from webelement import SeleniumDriver
from termcolor import colored


class LogInPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _email_field = '//*[@id="identifierId"]'
    _password_field = '//*[@id="password"]/div[1]/div/div[1]/input'
    _email_next_button = '//*[@id="identifierNext"]'
    _password_next_button = '//*[@id="passwordNext"]'
    _elem_for_check = '//*[@id=":8h"]/div[1]/div'

    def clickLoginLink(self):
        self.elementClick(self._email_field)

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickEmailNext(self):
        self.elementClick(self._email_next_button)

    def clickPasswordNext(self):
        self.elementClick(self._password_next_button)

    def checkLogIn(self):
        return self.isElementPresent(self._elem_for_check)
        # print('User is successfully logged in. Compose button is present on the page')

    def nextPasswordButtonChecker(self):
        return self.isElementPresent(self._password_next_button)

    def login_valid(self, email="testqwerty6970@gmail.com", password="test_passWORD713"):
        """
        :param username = user's email:
        :param password = password to email:
        """
        self.clickLoginLink()
        self.enterEmail(email)
        self.clickEmailNext()
        self.enterPassword(password)
        self.clickPasswordNext()
        if self.checkLogIn() is True:
            print(colored('Valid LogIn test - Passed', 'green'))
        else:
            print(colored('Valid LogIn test - Failed', 'red'))

        self.driver.quit()

    def login_invalid_email(self, email='someemail@gmail.com'):
        """
        :param invalid email:

        """
        self.clickLoginLink()
        self.enterEmail(email)
        self.clickEmailNext()
        if self.nextPasswordButtonChecker() is True:
            self.driver.quit()
            print(colored('Negative test with wrong email - Passed', 'green'))
        else:
            print(colored('Negative test with wrong email - Failed', 'red'))
            self.driver.quit()

    def login_invalid_password(self, email="testqwerty6970@gmail.com", password="invalidpassword"):
        """
        :param valid email:
        :param invalid password:
        """
        self.clickLoginLink()
        self.enterEmail(email)
        self.clickEmailNext()
        self.enterPassword(password)
        self.clickPasswordNext()
        if self.checkLogIn() is False:
            print(colored('Negative test with wrong password - Failed', 'red'))
        else:
            print(colored('Negative test with wrong password - Passed', 'green'))
            self.driver.quit()





























#     email_raw = WebElement(driver).create_web_element('//*[@id="identifierId"]')
#
#     email_next_button = WebElement(driver).create_web_element('//*[@id="identifierNext"]')
#
#     password_field = WebElement(driver).create_web_element('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div'
#                                                            '/content/form/div[1]/div/div[1]/div/div[1]/input')
#
#     forgot_password_button = WebElement(driver).create_web_element('//*[@id="forgotPassword"]')
#
#     password_next_button = WebElement(driver).create_web_element('//*[@id="passwordNext"]')
#
#     logged_in_checker = WebElement(driver).create_web_element('//*[@id=":8h"]/div[1]/div')
#
#     def log_in_valid_check(self):
#         driver.implicitly_wait(30)
#         self.email_raw.click()
#         self.email_raw.clear()
#         self.email_raw.fill_in('testqwerty6970@gmail.com')
#         self.email_next_button.click()
#         self.password_field.fill_in("test_passWORD713")
#         self.password_next_button.click()
#         self.inbox_button.click()
#
#
# new_page = LogInPage()
#
# new_page.log_in_valid_check()