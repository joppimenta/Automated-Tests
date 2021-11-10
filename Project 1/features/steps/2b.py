from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

@given("the user is on the platform login page and the high contrast mode is activated")
def given(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

@when("the user logins on the DAL platform, goes to the home page and click on the High Contrast mode button 2")
def when(context):
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("joao.pimenta@dellead.com")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("abcd1234")

    login_button = context.driver.find_element_by_id("login-btn")
    login_button.click()

    sleep(5)

    highcontrast_button = context.driver.find_element_by_id("bt-highContrast")
    highcontrast_button.click()

@then("the High Contrast mode is disabled")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@aria-label='Enable high contrast']")))

    context.driver.quit()
