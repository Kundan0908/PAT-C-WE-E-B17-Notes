from selenium.webdriver.common.by import By
class Login:
    def __init__(self,driver):
        self.driver = driver
        self.username_loc = By.NAME,'username' # By.Name,'username' ->(name,username)
        self.password_loc = (By.NAME,'password')
        self.login_btn_loc = (By.TAG_NAME,'button')
        self.forgot_pwd_loc = (By.XPATH,'orangehrm-login-forgot-header')

    def navigate_url(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    def login_(self):
        self.driver.find_element(*self.username_loc ).send_keys('Admin') # find_element((By.Name,'username'))
        self.driver.find_element(*self.password_loc).send_keys('admin123') # find_element(By.NAME,'password')
        self.driver.find_element(*self.login_btn_loc).click()
        return self.driver.title

    def forgot_pwd(self):
        self.driver.find_element(*self.forgot_pwd_loc).click()