# Name: login_steps.py
# Copyright 2015, Opex Software
# Apache License, Version 2.0
# This is a behave step-definitions file containing implementations of GWT's feature steps

import time
from behave import *
from features.pages.login_page import LoginPage


@step('I follow {link} link in account section')
def step(context, link):
    login=LoginPage(context.driver)
    login.account_section.click()
    time.sleep(1)
    if link == "login":
        print("It came here")
        login.login_link.click()
    elif link == "register":
        login.register_link.click()


@when('I login with username "{uname}" and password "{pwd}"')
def step(context, uname, pwd):
    log=LoginPage(context.driver)
    log.login(uname, pwd)


@when('I logout')
def step(context):
    login = LoginPage(context.driver)
    login.logout()


@then('I should see {type} message for {action}')
def step(context,type,action):
    login = LoginPage(context.driver)
    if action == "login":
        if type == "invalid_credentials":
            assert login.error_message.text == "Invalid login or password."
        elif type == "mandatory_fields":
            time.sleep(1)
            login.verify_mandatory_fields_message(action)
    elif action == "registration":
        if type == "mandatory_fields":
            time.sleep(1)
            login.verify_mandatory_fields_message(action)
        elif type == "existing_user":
            assert login.error_message.text == "There is already an account with this email address. If you are sure that it is your email address, click here to get your password and access your account."
        elif type == "new_user":
            assert login.success_message.text == "Thank you for registering with Main Website Store."


@when('I register {type} user')
def step(context,type):
    login = LoginPage(context.driver)
    login.register_user(type)