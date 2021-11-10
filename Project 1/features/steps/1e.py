from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

@given("the user is on the platform login page 6")
def given(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

@when("the user logins on the DAL platform, clicks on the Color Palette button and changes the background color")
def when(context):
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("joao.pimenta@dellead.com")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("abcd1234")

    enter_button = context.driver.find_element_by_id("login-btn")
    enter_button.click()

    sleep(3)

    colorpallete_button = context.driver.find_element_by_id("bt-accessibility-pallete")
    colorpallete_button.click()

    sleep(3)

    yellowcolor = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/app-header/header/app-accessibility-bar/nav/div/div/app-wal-accessibility-functions/div/div/div[2]/div[1]/div/ul/li[6]")
    yellowcolor.click()



@then("the background color of the platform changes to the color chosen by the user")
def then(context):
    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_any_elements_located((By.XPATH, "//div[@style = 'background-color: rgb(252, 220, 0) !important;']")))