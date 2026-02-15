# class ABC:
#     class_name = 'B16-B17'
#
#     def __init__(self,name,age=22):
#         self.name = name # object/instance variables
#         self.age = age
# #
# obj1 = ABC('venkat')
# obj2 = ABC('venkat',23)
# print(obj1.age)
# print(obj2.age)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.get('https://www.worldometers.info/world-population/')

wait = WebDriverWait(driver,10)
population = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[@id='maincounter-number']")))
print(population.text)
