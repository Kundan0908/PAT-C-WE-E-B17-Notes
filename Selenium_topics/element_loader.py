import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://www.automationtesting.co.uk/loader.html')

wait = WebDriverWait(driver,10)
print(wait.until(expected_conditions.visibility_of_element_located((By.ID,'loaderBtn'))).text)
driver.quit()