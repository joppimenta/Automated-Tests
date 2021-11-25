from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from time import sleep


@given("the user is on the SGME login page, logins on the platform using valid credentials, goes to the ‘Users’ section and clicks on the ‘Create user’ button")
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

    users_button = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/nav/div/div[2]/ul[1]/li[3]/a/span")
    users_button.click()

    WebDriverWait(context.driver, 60).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-users/div/div/app-custom-card/div/div[1]/span[1]/span"), "LISTA DE USUÁRIOS CADASTRADOS"))
    createUser_button = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-users/div/div/app-custom-card/div/div[2]/div/div/div[1]/div/a[1]")
    createUser_button.click()

    WebDriverWait(context.driver, 60).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-create-user/div/app-custom-card/div/div[1]/span[1]/span"), "ADICIONAR USUÁRIO"))

@when("the user fills the blank fields and clicks on the ‘Save data’ button")
def when(context):
    username_field = context.driver.find_element_by_id("name")
    username_field.send_keys("TEST USER 198700")

    phone_field = context.driver.find_element_by_id("phone")
    phone_field.send_keys("8594261123")

    email_field = context.driver.find_element_by_id("email")
    email_field.send_keys("testusuario97949@gmail.com")

    select = Select(context.driver.find_element_by_id("language"))
    select.select_by_value("1: Object")

    permission_box = Select(context.driver.find_element_by_id("profile"))
    permission_box.select_by_value("1: Object")

    country_box = Select(context.driver.find_element_by_id("country"))
    country_box.select_by_value("3: Object")

    sleep(4)

    state_box = Select(context.driver.find_element_by_id("state"))
    state_box.select_by_value("2: Object")

    sleep(3)

    save_button = context.driver.find_element_by_id("save")
    save_button.click()

@then("the user is created")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-sidebar-layout/div/div/app-alert-system/div/div/div[1]")))
