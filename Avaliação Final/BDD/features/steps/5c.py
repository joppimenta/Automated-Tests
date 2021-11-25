from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep


@given("the user is on the SGME login page, logins on the platform using valid credentials, goes to the ‘Companies’ section and clicks on the ‘More options’ button 1")
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

    moreOptions_button = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-list-companies/div/div/app-custom-card/div/div[2]/div/div/div[2]/div[1]/app-filter-companies/div/div/table/tbody/tr/td[5]/app-filter-actions/div/button[1]")
    moreOptions_button.click()

@when("the user inputs on the ‘Year’ field ‘2023’ and clicks on the ‘Search’ button")
def when(context):
    year_field = context.driver.find_element_by_id("year")
    year_field.send_keys("2023")

    search_button = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-list-companies/div/div/app-custom-card/div/div[2]/div/div/div[2]/div[1]/app-filter-companies/div/div/table/tbody/tr[1]/td[5]/app-filter-actions/div/button[2]")
    search_button.click()

    sleep(3)

@then("a company with the searched year appears on the companies table")
def then(context):

    more_button = context.driver.find_element_by_xpath("/html/body/app-root/app-sidebar-layout/div/div/app-administrator/div/app-list-companies/div/div/app-custom-card/div/div[2]/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td[7]/app-collapse-caret/button/span")
    more_button.click()

    sleep(3)

    WebDriverWait(context.driver, 60).until(expected_conditions.text_to_be_present_in_element((By.XPATH, "//*[@id='collapse0']/td[1]"), "2023"))
