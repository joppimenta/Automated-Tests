from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

@given("the user is in the platform login page")
def given(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

@when("the user logins on the DAL platform, goes to the home page and click on the High Contrast mode button")
def when(context):
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("joao.pimenta@dellead.com")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("abcd1234")

    enter_button = context.driver.find_element_by_id("login-btn")
    enter_button.click()

    sleep(7)

    highcontrast_button = context.driver.find_element_by_id("bt-highContrast")
    highcontrast_button.click()


@then("the high contrast mode is activated")
def then(context):

    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@aria-label='Disable high contrast']")))

    context.driver.quit()
