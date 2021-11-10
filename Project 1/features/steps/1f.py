from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
import pyautogui


@given("the user is on the platform login page 8")
def given(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

@when("the user logins on the platform, goes to the Edit Profile zone, clicks on the Change Photo button and selects a profile picture")
def when(context):
    username_field = context.driver.find_element_by_id("login")
    username_field.send_keys("joao.pimenta@dellead.com")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("abcd1234")

    enter_button = context.driver.find_element_by_id("login-btn")
    enter_button.click()

    sleep(3)

    profile_button = context.driver.find_element_by_id("avatar")
    profile_button.click()

    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-sidebar-layout/app-header/header/app-accessibility-bar/nav/div/div/div/div/div[2]/div[1]/p/a")))

    editProfile_button = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/app-header/header/app-accessibility-bar/nav/div/div/div/div/div[2]/div[1]/button")
    editProfile_button.click()

    WebDriverWait(context.driver, 50).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-profile/form/div[1]/h3"), "Dados Pessoais"))

    addPhoto_button = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-profile/form/div[2]/div[1]/div[1]/button")
    addPhoto_button.click()

    context.driver.find_element_by_id("IdOfInputTypeFile").send_keys(os.getcwd() + "/170-1704708_unit-jotaro-kujo-jojos-bizarre-adventure.png")


@then("the photo chosen by the user becomes their profile photo")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/div/app-alert/div/div/div[1]")))
