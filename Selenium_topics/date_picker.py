from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://www.automationtesting.co.uk/datepicker.html')
driver.maximize_window()

driver.find_element(By.ID,'basicDate').click()
date_time_picker = driver.find_elements(By.XPATH,"//div[@class='dayContainer']/span")
for each_date in date_time_picker:
    if each_date.text == '12':
        each_date.click()
        driver.find_element(By.TAG_NAME,'body').click()
        break


