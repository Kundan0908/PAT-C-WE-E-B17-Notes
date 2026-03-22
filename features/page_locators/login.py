from selenium.webdriver.common.by import By

class Login:
    def __init__(self,driver):
        self._username_loc = (By.NAME,'user-name') # username field locator
        self._password_loc = (By.NAME,'password')  # password field locator
        self._login_loc = (By.NAME,'login-button') # login field locator
        self._item_header_loc = (By.XPATH,'//span[@class="title"]') # item header locator
        self.driver = driver

    def navigate_url(self,url):
        try:
            self.driver.get(url)
            return True
        except:
            raise Exception ("Error in navigating to login page")

    def enter_username_details(self,username):
        self.driver.find_element(*self._username_loc).send_keys(username)

    def enter_password_details(self,password):
        self.driver.find_element(*self._password_loc).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self._login_loc).click()
        try:
            get_item_header = self.driver.find_element(*self._item_header_loc).text
            return get_item_header
        except:
            raise Exception("Error in login page")
