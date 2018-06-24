from webelement import WebElement
from test import driver


class LogInPage():

    email_raw = WebElement(driver).create_web_element('//*[@id="identifierId"]')

    email_next_button = WebElement(driver).create_web_element('//*[@id="identifierNext"]')

    password_field = WebElement(driver).create_web_element('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div'
                                                           '/content/form/div[1]/div/div[1]/div/div[1]/input')

    forgot_password_button = WebElement(driver).create_web_element('//*[@id="forgotPassword"]')

    password_next_button = WebElement(driver).create_web_element('//*[@id="passwordNext"]')

    logged_in_checker = WebElement(driver).create_web_element('//*[@id=":8h"]/div[1]/div')

    def log_in_valid_check(self):
        driver.implicitly_wait(30)
        self.email_raw.click()
        self.email_raw.clear()
        self.email_raw.fill_in('testqwerty6970@gmail.com')
        self.email_next_button.click()
        self.password_field.fill_in("test_passWORD713")
        self.password_next_button.click()
        self.inbox_button.click()
        driver.quit()

new_page = LogInPage()

new_page.log_in_valid_check()