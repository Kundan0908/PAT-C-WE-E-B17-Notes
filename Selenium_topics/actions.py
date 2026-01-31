import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get('https://www.automationtesting.co.uk/actions.html')

action =  ActionChains(driver)
time.sleep(2)
# source = driver.find_element(By.XPATH,"(//div[@class='droptarget'])[1]")
# target = driver.find_element(By.XPATH,"(//div[@class='droptarget'])[2]")
# action.drag_and_drop(source=source,target=target).perform()

# double_click_element = driver.find_element(By.ID,'doubleClickArea')
# action.double_click(double_click_element).perform()

# holding_element_loc = driver.find_element(By.ID,'holdDown')
# action.click_and_hold(holding_element_loc).perform()
# action.release(holding_element_loc).perform()

hold_shift_element_loc = driver.find_element(By.XPATH,"//p[text()='Hold Shift & Click Here']")
action.key_down(Keys.SHIFT)
action.click_and_hold(hold_shift_element_loc).perform()
# action.send_keys_to_element(hold_shift_element_loc,Keys().SHIFT).perform()


