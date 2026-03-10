from behave import given, when,then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('User navigates to url')
def step_impl(context):
    context.driver = webdriver.Firefox()
    context.driver.get("https://www.saucedemo.com/")

@when('User enters the username "{user_name}"')
def step_impl(context,user_name):
    context.driver.find_element(By.NAME,'user-name').send_keys(user_name)

@when('User enters the password "{password}"')
def step_impl(context,password):
    context.driver.find_element(By.NAME,'password').send_keys(password)

@when('I click on login button')
def step_impl(context):
    context.driver.find_element(By.NAME,'login-button').click()

@then('I should be able to reach dashboard page')
def step_impl(context):
    product_page = context.driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/span').text
    if product_page == 'Products':
        print("Dashboard page visible")
    else:
        raise Exception ("Product not visible")
