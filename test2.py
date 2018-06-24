from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('driver/chromedriver')
driver.implicitly_wait(30)
driver.maximize_window()
driver.delete_all_cookies()





