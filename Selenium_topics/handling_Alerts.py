import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://www.selenium.dev/selenium/web/alerts.html#')
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID, "prompt").click()
time.sleep(2)
driver.switch_to.alert.send_keys('test')
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element(By.ID, "prompt").click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)