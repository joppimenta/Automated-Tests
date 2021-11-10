from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@given("the user is in the LEAD platform login page")
def given(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

@when("the user input invalid credentials")
def when(context):
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("joaoteste19853210")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("1953210")

    enter_button = context.driver.find_element_by_id("login-btn")
    enter_button.click()

@then("LEAD platform reports an error on the login page")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-login/html/body/form/div[1]')))
    context.driver.quit()
