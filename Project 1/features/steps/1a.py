from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@given("a user is in the LEAD platform login page")
def given(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

@when("the user input his valid credentials")
def when(context):
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("joao.pimenta@dellead.com")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("abcd1234")

    login_button = context.driver.find_element_by_id("login-btn")
    login_button.click()

@then("LEAD platform redirects the user to the home page")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-sidebar-layout/nav/ul/div/li[1]/a[1]')))

    context.driver.quit()
