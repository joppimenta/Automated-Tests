from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from time import sleep

@given("the user is on the platform login page 5")
def given(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://homologacao.leadfortaleza.com.br/ead/login")
    context.driver.maximize_window()

@when("the user clicks on the Create Profile button and fills in the blank fields")
def when(context):
    create_button = context.driver.find_element_by_xpath("/html/body/app-root/app-login/html/body/form/div[5]/button")
    create_button.click()

    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-preselectionsignup/div/app-small-header/div/div[2]/h2')))

    name_field = context.driver.find_element_by_id("name")
    name_field.send_keys("USER TEST AAA")

    email_field = context.driver.find_element_by_id("email")
    email_field.send_keys("usertest197@gmail.com")

    cpf_field = context.driver.find_element_by_id("cpf")
    cpf_field.send_keys("382.856.070-97")

    phone_field = context.driver.find_element_by_id("phone")
    phone_field.send_keys("54302887583")
    
    birthdate_field = context.driver.find_element_by_id("birthdate")
    birthdate_field.send_keys("06021997")

    gender_box = Select(context.driver.find_element_by_id("gender"))
    gender_box.select_by_visible_text("Feminino")
    sleep(0.8)

    country_box = Select(context.driver.find_element_by_id("country"))
    country_box.select_by_visible_text("Brasil")

    state_box = Select(context.driver.find_element_by_id("state"))
    state_box.select_by_visible_text("Ceará")

    city_box = Select(context.driver.find_element_by_id("city"))
    city_box.select_by_visible_text("FORTALEZA")

    username_field = context.driver.find_element_by_id("username")
    username_field.send_keys("test_user_4823")

    password_field = context.driver.find_element_by_id("password")
    password_field.send_keys("abcd1234")

    confirmpassword_field = context.driver.find_element_by_id("confirmPassword")
    confirmpassword_field.send_keys("abcd1234")

    disability_box = Select(context.driver.find_element_by_id("disabilityProfile"))
    disability_box.select_by_visible_text("Nenhuma")

    checkbox1 = context.driver.find_element_by_xpath("/html/body/app-root/app-preselectionsignup/div/app-small-header/form/div[6]/input")
    checkbox1.click()

    checkbox2 = context.driver.find_element_by_xpath("/html/body/app-root/app-preselectionsignup/div/app-small-header/form/div[7]/input")
    checkbox2.click()

    save_button = context.driver.find_element_by_xpath("/html/body/app-root/app-preselectionsignup/div/app-small-header/form/div[8]/button")
    save_button.click()

@then("the account is created")
def then(context):
    WebDriverWait(context.driver, 50).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-confirm-preselection/div/div/div/div[1]/h2")))