from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome('driver/chromedriver')
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://www.gmail.com")

driver.find_element(By.XPATH, '//*[@id="identifierId"]').click()
driver.find_element(By.XPATH, '//*[@id="identifierId"]').clear()
driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys("testqwerty6970@gmail.com")
driver.find_element_by_css_selector("#identifierNext > content > span").click()
driver.find_element_by_css_selector(".whsOnd.zHQkBf[type=password]").send_keys("test_passWORD713")
driver.find_element_by_css_selector("#passwordNext > content > span").click()
driver.find_element(By.XPATH, '/html/body/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div/div[1]'
                              '/div/div[]')
driver.quit()






