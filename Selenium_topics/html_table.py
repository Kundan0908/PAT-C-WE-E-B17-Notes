import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


option = Options()
option.add_argument('--private')
option.add_argument('--headless')
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),options=option)
driver.get('https://www.automationtesting.co.uk/tables.html')
time.sleep(2)

table_loc = driver.find_elements(By.XPATH," //table[@class='sortable']/tbody/tr/td")
for each_table in table_loc:
    print(each_table.text)



