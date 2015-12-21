# Name =  checkout_page.py
# Copyright 2015, Opex Software
# Apache License, Version 2.0
# This is a page object file for Magento Checkout page containing web-elements and its interactive methods

import os
from page_objects import PageObject, PageElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import randint
from faker import Faker

class CheckoutPage(PageObject):

    proceed_to_checkout = PageElement(css = "button[title*='Proceed to Checkout']")
    checkout_as_guest_radio = PageElement(id_ = "login:guest")
    checkout_continue_button = PageElement(id_ = "onepage-guest-register-button")
    page_primary_message =  PageElement(css = "div.page-title h1")
    page_secondary_message = PageElement(css = "h2")

    billing_first_name = PageElement(id_ = "billing:firstname")
    billing_last_name = PageElement(id_ = "billing:lastname")
    billing_email = PageElement(id_ = "billing:email")
    billing_address = PageElement(id_ = "billing:street1")
    billing_city = PageElement(id_ = "billing:city")
    billing_state = PageElement(id_ = "billing:region_id")
    billing_zip = PageElement(id_ = "billing:postcode")
    billing_country = PageElement(id_ = "billing:country_id")
    billing_phone = PageElement(id_ = "billing:telephone")
    billing_continue_button = PageElement(css = "#billing-buttons-container button")
    shipping_method_continue_button = PageElement(css = "#shipping-method-buttons-container button")

    payment_check = PageElement(id_ = "p_method_checkmo")
    payment_cc = PageElement(id_ = "p_method_ccsave")
    payment_cod = PageElement(id_ = "p_method_cashondelivery")
    payment_continue_button = PageElement(css = "#payment-buttons-container button")
    cc_name = PageElement(id_ = "ccsave_cc_owner")
    cc_type = PageElement(id_ = "ccsave_cc_type")
    cc_number = PageElement(id_ = "ccsave_cc_number")
    cc_expiration_month = PageElement(id_ = "ccsave_expiration")
    cc_expiration_year = PageElement(id_ = "ccsave_expiration_yr")

    place_order_button = PageElement(css = "button.btn-checkout")


    def __init__(self,driver):
        super(CheckoutPage,self).__init__(driver)
        self.driver = driver


    def add_product_to_cart(self,type):
        if type == "RUN_INDEX":
            if "RUN_INDEX" not in os.environ:
                index = randint(0,2)
            else:
                index = int(os.environ.get("RUN_INDEX"))%3

            if index == 0:
                index = 3
        else:
            index = int(type)

        self.driver.find_element(By.XPATH, "//ul[contains(@class,'products-grid')]/li[" + str(index) + "]//button").click()


    def fill_and_submit_billing_information(self,type):
        self.select_dropdown_value_by_text(self.billing_country,"India")
        faker = Faker()
        if type == "guest":
            self.billing_first_name = faker.first_name()
            self.billing_last_name = faker.last_name()
            self.billing_email = faker.email()

        self.billing_address = "Turning Point II"
        self.billing_city = "Pune"
        self.billing_zip = "411014"
        self.billing_phone = "02026632223"
        self.billing_continue_button.click()


    def select_dropdown_value_by_text(self,webelement,text):
        select = Select(webelement)
        select.select_by_visible_text(text)


    def continue_with_shipping_method(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#shipping-method-buttons-container button")))
        self.shipping_method_continue_button.click()

    def fill_credit_card_information(self):
        self.select_dropdown_value_by_text(self.cc_type, "Visa")
        self.cc_name = "Opex Software"
        self.cc_number = "4111111111111111"
        self.select_dropdown_value_by_text(self.cc_expiration_month, "11 - November")
        self.select_dropdown_value_by_text(self.cc_expiration_year, "2025")

    def verify_order_confirmation_message(self):
        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located((By.XPATH, "//button[@title='Continue Shopping']")))
        assert self.driver.find_element(By.TAG_NAME, "h1").text == "YOUR ORDER HAS BEEN RECEIVED."
        assert self.driver.find_element(By.TAG_NAME, "h2").text == "THANK YOU FOR YOUR PURCHASE!"
