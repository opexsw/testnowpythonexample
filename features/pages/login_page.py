# Name =  login_page.py
# Copyright 2015, Opex Software
# Apache License, Version 2.0
# This is a page object file for Magento Checkout page containing web-elements and its interactive methods


import os
from page_objects import PageObject, PageElement
from faker import Factory, Faker

class LoginPage(PageObject):

    account_section = PageElement(css = "a.skip-account")
    login_link = PageElement(xpath = "//a[@title='Log In']")
    logout_link = PageElement(xpath = "//a[@title='Log Out']")
    register_link = PageElement(xpath = "//a[@title='Register']")

    username = PageElement(id_ = "email")
    password = PageElement(id_ = "pass")
    login_button = PageElement(id_ = "send2")
    error_message = PageElement(css = "li.error-msg span")
    success_message = PageElement(css = "li.success-msg span")
    mandatory_email_message = PageElement(id_ = "advice-required-entry-email")
    mandatory_password_message = PageElement(id_ = "advice-required-entry-pass")
    
    register_button = PageElement(xpath = "//button[@title='Register']")
    first_name_textbox = PageElement(id_ = "firstname")
    last_name_textbox = PageElement(id_ = "lastname")
    email_address_textbox = PageElement(id_ = "email_address")
    password_textbox = PageElement(id_ = "password")
    confirm_password_textbox = PageElement(id_ = "confirmation")
    mandatory_first_name_message = PageElement(id_ = "advice-required-entry-firstname")
    mandatory_last_name_message = PageElement(id_ = "advice-required-entry-lastname")
    mandatory_email_address_message = PageElement(id_ = "advice-required-entry-email_address")
    mandatory_register_password_message = PageElement(id_ = "advice-required-entry-password")
    mandatory_confirm_password_message = PageElement(id_ = "advice-required-entry-confirmation")

    def __init__(self,driver):
        super(LoginPage,self).__init__(driver)
        self.driver = driver

    def go_to_homepage(self):
        self.driver.get(os.getenv("TEST_URL", "https://104.131.191.140"))

    def login(self, uname, pwd):
        self.username = uname
        self.password = pwd
        self.login_button.click()

    def logout(self):
        self.account_section.click()
        self.logout_link.click()


    def verify_mandatory_fields_message(self,action):
        message = "This is a required field."
        if action == "login":
            assert self.mandatory_email_message.text == message
            assert self.mandatory_password_message.text == message
        elif action == "registeration":
            assert self.mandatory_first_name_message.text == message
            assert self.mandatory_last_name_message.text == message
            assert self.mandatory_email_address_message.text == message
            assert self.mandatory_register_password_message.text == message
            assert self.mandatory_confirm_password_message.text == message


    def register_user(self, type):
        fake = Faker()
        self.first_name_textbox = fake.first_name()
        self.last_name_textbox = fake.last_name()
        self.password_textbox = "password123"
        self.confirm_password_textbox = "password123"
        if type == "new":
            email = fake.email()
            self.email_address_textbox = email
            return email
        elif type == "existing":
            self.email_address_textbox = "admin@mailinator.com"
