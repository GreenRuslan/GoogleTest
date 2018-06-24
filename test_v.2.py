from selenium import webdriver
from loginpage import LogInPage


class LoginTest:

    def test_validLogin(self):
        baseURL = "http://www.gmail.com"
        driver = webdriver.Chrome('driver/chromedriver')
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get(baseURL)

        lp = LogInPage(driver)
        lp.login_valid()

    def test_invalid_email_logIn_(self):
        baseURL = "http://www.gmail.com"
        driver = webdriver.Chrome('driver/chromedriver')
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseURL)

        lp = LogInPage(driver)
        lp.login_invalid_email()

    def test_invalid_password_logIn(self):
        baseURL = "http://www.gmail.com"
        driver = webdriver.Chrome('driver/chromedriver')
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseURL)

        lp = LogInPage(driver)
        lp.login_invalid_password()


pp = LoginTest()
# pp.test_validLogin()
pp.test_invalid_email_logIn_()
# pp.test_invalid_password_logIn()


