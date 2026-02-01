from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.firefox import GeckoDriverManager

# Absolute xpath: starts from html tag with '/' and goes till the very end of the node tag of required locator

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://www.automationtesting.co.uk/index.html')
# print(driver.find_element(By.XPATH,'/html/body/div/div/div/section/div/header/p[2]/a').text)

# Relative xpath: starts with '//' and follows syntax of //tag-name[@attribute='value']
# print(driver.find_element(By.XPATH,'//p[3]/a').text)

# comparing absolute and relative xpath together

abs_xpath_for_courses_loc = '/html/body/div/div/div/section/div/div/article/div[2]/h3/a'
rel_xpath_for_courses_loc = '//article/div[2]/h3/a'

lst_of_courses_loc = driver.find_elements(By.XPATH,abs_xpath_for_courses_loc) # abs_xpath_for_courses_loc with rel_xpath_for_courses_loc and execute, result will be same
for each_course in lst_of_courses_loc:
    print(each_course.text)
driver.quit()

# xpaths for parent-child
# //div[@class='content']/child::h3 -> child abbrevation should be used following by :: child-tag name

# xpaths for siblings
# 1. Following-siblings : siblings which are below the referenced sibling xpath
# //article[1]//child::div[1]/following-sibling::div

# 2. Preceding-siblings: siblings which are above the referenced sibling xpath
# //article[1]//child::div[2]/preceding-sibling::div

# xpaths for child-parent : For this navigation give parent or grand parents tag-name and attribute value along
# //div[2]/ancestor::div[@class='content']

# xpaths for child-great grand parents : This will navigate to the beginning of the node for the given tag
# //div[2]/ancestor::div

# use of and in xpath writing : We need to provide xpaths which should have both conditions true inside square brackets
# //div[@id='sidebar' and @class='inactive'] -> This will check for any one id to be present

# use of or in xpath writing : We need to provide xpaths which has either condition true inside square brackets
# //div[@id='sidebar' and @class='inactive'] -> This will check for any one id to be present

# using contains in xpath locator: It checks for matching string for the tag-name and attribute value in the webpage
# //div[contains(@class,'col')]



