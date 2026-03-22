import time
import pdb
from behave import given, when,then
from features.page_locators.login import Login
from features.page_locators.products import Products
from features.login_data.read_json_data import usrname,pswrd
from selenium import webdriver
from features.login_data.read_excel_data import username,password
from selenium.webdriver.common.by import By

@given('User is able to reach login url (# prerequisite step)')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.login_page = Login(driver=context.driver) # login_ = Login()
    context.login_page.navigate_url("https://www.saucedemo.com/")
    # context.driver.get("https://www.saucedemo.com/")

@when('User enters username in the username field "{username}"')
def step_impl(context,username):
    context.login_page.enter_username_details(username = username)
    # context.driver.find_element(By.NAME,'user-name').send_keys(username)

@when('User enters password in the password field "{password}"')
def step_impl(context,password):
    context.login_page.enter_password_details(password=password)
    # context.driver.find_element(By.NAME,'password').send_keys(password)

@when('User clicks on the login button')
def step_impl(context):
    context.login_page.click_login()
    # context.driver.find_element(By.NAME,'login-button').click()

@when('User is able to pick item "{item}" and click on add to cart button')
def step_impl(context,item):
    context.products = Products(context.driver)
    time.sleep(3)
    context.products.selecting_items(item)

@when('User enters username in the username field from excel-sheet')
def step_impl(context):
    context.login_page.enter_username_details(username=username)

@when('User enters password in the password field from excel-sheet')
def step_impl(context):
    context.login_page.enter_password_details(password=password)

@when('User enters username in the username field from json file')
def step_impl(context):
    context.login_page.enter_username_details(username=usrname)

@when('User enters password in the password field from json file')
def step_impl(context):
    context.login_page.enter_password_details(password=pswrd)

@then("User should be navigated to the landing page")
def step_impl(context):
    landing_page = context.driver.find_element(By.XPATH,'//span[@class="title"]').text
    assert landing_page == 'Products','Unable to login, Testcase failed'
    context.driver.quit()

@then ('User should not be navigated to the login page')
def step_impl(context):
    context.driver.find_element(By.NAME, 'login-button').click()
    error_message = context.driver.find_element(By.XPATH,'//h3[@data_old-test="error"]').text
    assert error_message == 'Epic sadface: Username and password do not match any user in this service','Able to login, Testcase failed'
    context.driver.quit()

@then('User should be able to verify item added to cart')
def step_impl(context):
    context.products.validate_item_added_cart()
