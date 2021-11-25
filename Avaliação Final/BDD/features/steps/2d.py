from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys

from time import sleep

@given("the user is on the SGME login page, logins on the platform using valid credentials and goes to the ‘Profile’ section 2")
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


    profile_button = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/nav/div/div[2]/ul[3]/li[1]/a/span")
    profile_button.click()

    WebDriverWait(context.driver, 60).until(expected_conditions.url_changes("https://test.jasgme.com/pt/profile"))

@when("the user clicks on the ‘Change password’ button and inputs on the ‘New password’ and ‘Confirm password’ the passwords: ‘abcd1234’ and ‘abcd1230’, respectively")
def when(context):
    elm = context.driver.find_element_by_tag_name('html')
    elm.send_keys(Keys.END)
    sleep(10)

    change_button = context.driver.find_element_by_id("change")
    change_button.click()

    password2_field = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-profile/div/div/app-custom-card[2]/div/div[2]/div/form/div[4]/div/div[1]/div/input")
    password2_field.send_keys("abcd1234")

    confirmPassword_field = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-profile/div/div/app-custom-card[2]/div/div[2]/div/form/div[4]/div/div[2]/div/input")
    confirmPassword_field.send_keys("abcd1230")

@then("an error message appears on the screen")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-profile/div/div/app-custom-card[2]/div/div[2]/div/form/div[4]/small"), "As senhas não conferem!"))
