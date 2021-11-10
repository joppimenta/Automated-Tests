from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

@given("the user is on the platform login page 4")
def given(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

@when("the user clicks on the 'Forgot your password' button, puts an invalid email/username in the blank field and clicks on the 'Send Request' button")
def when(context):
    forgot_button = context.driver.find_element_by_xpath("//*[@id='footer']/a[1]")
    forgot_button.click()

    sleep(7)

    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("cdqwjklj@gmail.com")

    sendrequest_button = context.driver.find_element_by_id("send-btn")
    sendrequest_button.click()

@then("an error message appears on the screen")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.text_to_be_present_in_element((By.XPATH ,"//*[@id='recovery-body']/form/div[2]"), "Falha ao recuperar senha do usuario"))
    context.driver.quit()