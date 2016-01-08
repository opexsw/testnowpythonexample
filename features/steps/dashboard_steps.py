# Name: dashboard_steps.py
# Copyright 2015, Opex Software
# Apache License, Version 2.0
# This is a behave step-definitions file containing implementations of GWT's feature steps

import time
from behave import *
from selenium.webdriver.common.by import By
from features.pages.dashboard_page import DashboardPage

use_step_matcher("re")


@step('I edit (newsletter|contact|billing|shipping) section on My Dashboard page')
def step_implementation(context,section):
    context.driver.find_element(By.XPATH, "//h3[contains(text(),'" + section[:1].upper() + section[1:] + "')]/parent::div/a").click()


@step('I (de-select|select) General Subscription option')
def step_implementation(context,action):
    dash = DashboardPage(context.driver)
    dash.general_subscription(action)


@step('I enter a (fresh|registered) email id in newsletter subscriprion box')
def step_implementation(context,fresh_or_used):
    dash = DashboardPage(context.driver)
    dash.enter_newsletter_email(fresh_or_used)


@step('I should see (success|error) message for "([^"]*)" on(?: dashboard)? page')
def step_implementation(context,type,message):
    msg = context.driver.find_element(By.CSS_SELECTOR, "li." + type + "-msg span").text
    if message == "subscription_saved":
        assert msg == "The subscription has been saved."
    elif message == "subscription_removed":
        assert msg == "The subscription has been removed."
    elif message == "newsletter_subscription_saved":
        assert msg == "Thank you for your subscription."
    elif message == "newsletter_subscription_error":
        assert msg == "There was a problem with the subscription: This email address is already assigned to another user."

