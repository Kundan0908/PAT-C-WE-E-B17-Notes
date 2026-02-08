from POM.Invoking_browser import Browser
from login import Login

def test_login_scenario():
    launch_browser = Browser()
    firefox_browser = launch_browser.invoke_browser()
    user_login = Login(firefox_browser)
    user_login.navigate_url()
    title_of_page = user_login.login_()
    if title_of_page == 'OrangeHRM':
        print("Successfully logged in, TestCase Passed")
    else:
        print("Unable to logg in, TestCase Failed")
