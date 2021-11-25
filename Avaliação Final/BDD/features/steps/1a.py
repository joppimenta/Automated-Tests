from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

@given("the user is on the SGME login page")
def given(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://test.jasgme.com/pt/login")
    context.driver.maximize_window()

@when("the user clicks on recover password button, inputs his email or phone on the blank field and clicks on the ‘Request recovery’ button")
def when(context):

    forgotPassword_button = context.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/app-login-form/div[2]/div/div/div/form/div[3]/div[2]/a")
    forgotPassword_button.click()

    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-login/div/div/app-recovery/div[2]/div/div/div/div')))

    username_field = context.driver.find_element_by_xpath("/html/body/app-root/app-login/div/div/app-recovery/div[2]/div/div/div/div/input")
    username_field.send_keys("joao.pimenta@dellead.com")

    requestRecovery_button = context.driver.find_element_by_id("btnLogin")
    requestRecovery_button.click()

@then("a recovery email is sent to the user.")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.text_to_be_present_in_element((By.XPATH, '/html/body/app-root/app-login/div/div/app-recovery/div[2]/div/div/div/label/strong'), 'Solicitação realizada.'))