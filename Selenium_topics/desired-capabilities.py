from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
# options.add_argument('--headless')
options.add_argument('--Private') # replace with incognito for chrome
# options.add_argument('--width=650')
# options.add_argument('--height=1000')

options.add_argument('--window-size=1920,2000')
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),options=options)
driver.get('https://www.automationtesting.co.uk/index.html')
abs_xpath_for_courses_loc = '/html/body/div/div/div/section/div/div/article/div[2]/h3/a'
lst_of_courses_loc = driver.find_elements(By.XPATH,abs_xpath_for_courses_loc) # abs_xpath_for_courses_loc with rel_xpath_for_courses_loc and execute, result will be same
for each_course in lst_of_courses_loc:
    print(each_course.text)
driver.quit()

