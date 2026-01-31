import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class User:
    # url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    dashboard_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    username = 'Admin'
    password = 'admin123'

    def __init__(self,url):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.user_url = url

    def _login(self):
        try:
            self.driver.get(self.user_url)
            time.sleep(4)
            self.driver.find_element(By.NAME, 'username').send_keys(self.username)
            self.driver.find_element(By.NAME, 'password').send_keys(self.password)
            self.driver.find_element(By.TAG_NAME, 'button').click()
            time.sleep(4)
            page_url = self.driver.current_url
            assert page_url == self.dashboard_url, "URL mismatch"

        except Exception as e:
            print(f"Error in login page {e}")
            return False

        else:
            print("Logged in successfully")
            return True
