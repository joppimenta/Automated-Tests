from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep

@given("the user is on the platform login page 3")
def given(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

@when("the user clicks on the 'Forgot your password' button, puts your email/username on the username field and clicks on the 'Send Request' button")
def when(context):
    forgot_link = context.driver.find_element_by_xpath("//*[@id='footer']/a[1]")
    forgot_link.click()

    sleep(7)

    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("joao.pimenta@dellead.com")

    request_button = context.driver.find_element_by_id("send-btn")
    request_button.click()

    sleep(8)

@then("a password recovery email is sent to the user")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.text_to_be_present_in_element((By.XPATH, '/html/body/app-root/app-password-recovery/html/body/form/div[1]'), 'Instrucões para recuperação de senha foram enviados para o e-mail:'))
    context.driver.quit()
