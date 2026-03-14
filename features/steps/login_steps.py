from behave import given, when,then
from POM.login import Login
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('User is able to reach login url (# prerequisite step)')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://www.saucedemo.com/")

@when('User enters username in the username field "{username}"')
def step_impl(context,username):
    context.driver.find_element(By.NAME,'user-name').send_keys(username)

@when('User enters password in the password field "{password}"')
def step_impl(context,password):
    context.driver.find_element(By.NAME,'password').send_keys(password)

@when('User clicks on the login button')
def step_impl(context):
    context.driver.find_element(By.NAME,'login-button').click()

@then("User should be navigated to the landing page")
def step_impl(context):
    landing_page = context.driver.find_element(By.XPATH,'//span[@class="title"]').text
    assert landing_page == 'Products','Unable to login, Testcase failed'
    context.driver.quit()

@then ('User should not be navigated to the login page')
def step_impl(context):
    context.driver.find_element(By.NAME, 'login-button').click()
    error_message = context.driver.find_element(By.XPATH,'//h3[@data-test="error"]').text
    assert error_message == 'Epic sadface: Username and password do not match any user in this service','Able to login, Testcase failed'
    context.driver.quit()
