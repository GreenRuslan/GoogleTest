from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('driver/chromedriver')
driver.implicitly_wait(30)
driver.maximize_window()
driver.delete_all_cookies()
driver.get("http://www.gmail.com")

driver.find_element(By.XPATH, '//*[@id="identifierId"]').click()
driver.find_element(By.XPATH, '//*[@id="identifierId"]').clear()
driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys("testqwerty6970@gmail.com")
driver.find_element(By.XPATH, '//*[@id="identifierNext"]').click()
driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys("test_passWORD713")
driver.find_element(By.XPATH, '//*[@id="passwordNext"]').click()
driver.find_element(By.XPATH, '//*[@id=":8h"]/div[1]/div')
# driver.quit()






