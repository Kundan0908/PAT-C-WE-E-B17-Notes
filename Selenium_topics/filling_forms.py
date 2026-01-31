import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
actions = ActionChains(driver)
elem = driver.find_element(By.ID,'firstName')
actions.move_to_element(elem).perform()
elem.send_keys("demo")
time.sleep(2)

wait_ele = driver.find_element(By.CSS_SELECTOR,"label[for='gender-radio-2']")
driver.execute_script("arguments[0].scrollIntoView;", wait_ele)
# driver.execute_script("window.scrollBy(0,500)")
wait = WebDriverWait(driver, 10)
wait_ele = driver.find_element(By.CSS_SELECTOR,"label[for='hobbies-checkbox-2']")
driver.execute_script("arguments[0].scrollIntoView;", wait_ele)
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"label[for='gender-radio-2']"))).click()
# wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"label[for='hobbies-checkbox-2']"))).click()
driver.find_element(By.ID,'subjectsInput').send_keys("Phy")
ele = wait.until(EC.presence_of_element_located((By.XPATH,"//*[text()='Physics']")))
if ele.is_displayed():
    ele.click()
time.sleep(2)
driver.quit()