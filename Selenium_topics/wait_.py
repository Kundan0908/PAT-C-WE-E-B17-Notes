# Types of wait in selenium
# 1. Implicitly wait -> This wait is applied to all the web element of a page at the DOM level
# 2. Explicit wat -> The wait time for a specific web-element to appear on the screen

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://www.automationtesting.co.uk/loader.html')
driver.maximize_window()
driver.implicitly_wait(20)

print(driver.find_element(By.ID,'content').text)
print(driver.find_element(By.XPATH,"//div[@class='inner']/p").text)
# time.sleep(10)
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.visibility_of_element_located((By.ID,'loaderBtn'))).click()

