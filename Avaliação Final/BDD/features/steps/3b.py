from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

@given("the user is on the SGME login page and logins using valid credentials 3")
def given(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://test.jasgme.com/pt/login")
    context.driver.maximize_window()

    login_field = context.driver.find_element_by_id("login")
    login_field.send_keys("joao.pimenta@dellead.com")

    password_field = context.driver.find_element_by_id("inputPassword")
    password_field.send_keys("abcd1234")

    login_button = context.driver.find_element_by_id("btnLogin")
    login_button.click()

    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/nav/div/div[1]/div/div[2]/span")))

@when("the user clicks on the Decrease Font mode button")
def when(context):
    increaseFont_button = context.driver.find_element_by_id("bt-diminuir-fonte")
    increaseFont_button.click()

    sleep(4)

@then("the font size of the texts on the page is decreased")
def then(context):

    isdecreased = context.driver.find_element_by_xpath("//*[@style='font-size: 16px;']")

    resetFont_button = context.driver.find_element_by_id("bt-resetar-fonte") ##Gambiarra
    resetFont_button.click()