import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://www.automationtesting.co.uk/buttons.html')

action = ActionChains(driver)
move_to_bttn = driver.find_element(By.ID,'btn_three')
action.move_to_element(move_to_bttn).click().perform()
time.sleep(2)
driver.switch_to.alert.accept()

print(driver.find_element(By.ID,'btn_four').is_enabled())
