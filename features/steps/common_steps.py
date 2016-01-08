# Name: common_steps.py
# Copyright 2015, Opex Software
# Apache License, Version 2.0
# This is a behave step-definitions file containing implementations of GWT's feature steps

from behave import *
from features.pages.login_page import LoginPage
from features.pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By

use_step_matcher("re")

@step('I am on magento login page')
def step_implementation(context):
    login = LoginPage(context.driver)
    login.go_to_homepage()


@step('I should be on "([^"]*)" page')
def step_implementation(context,page):
    if page == "My Dashboard":
        assert context.driver.find_element(By.CSS_SELECTOR, "div.dashboard h1").text == page.upper()
    elif page == "Logout":
        assert "LOGGED OUT" in context.driver.find_element(By.CSS_SELECTOR, "div.page-title").text


@step('I click the ([^"]*) button')
def step_implementation(context,type):
    if type == "register":
        login = LoginPage(context.driver)
        login.register_button.click()
    elif type == "save":
        dash = DashboardPage(context.driver)
        dash.save_button.click()
    elif type == "subscribe":
        dash = DashboardPage(context.driver)
        dash.subscribe_button.click()


@step('I do a global search using "([^"]*)" keyword')
def step_implementation(context,keyword):
    dash = DashboardPage(context.driver)
    dash.do_a_global_search(keyword)


@step('I should see products')
def step_implementation(context):
    dash = DashboardPage(context.driver)
    dash.wait_for_products_to_be_displayed()