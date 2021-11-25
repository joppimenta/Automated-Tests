from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@given("the user is on the SGME login page, logins on the platform using valid credentials and goes to the ‘Companies’ section 4")
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


@when("the user inputs on the ‘Educational institution’ field ‘A Diego Institute’ and clicks on the ‘Search’ button")
def when(context):
    institute_field = context.driver.find_element_by_id("institution")
    institute_field.send_keys("A Diego Institute")

    search_button = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-list-companies/div/div/app-custom-card/div/div[2]/div/div/div[2]/div[1]/app-filter-companies/div/div/table/tbody/tr/td[5]/app-filter-actions/div/button[2]")
    search_button.click()

@then("a company with the searched institution appears on the companies table")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//*[@id='body']/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td[5]"), "A Diego Institute"))