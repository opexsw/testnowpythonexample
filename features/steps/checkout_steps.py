# Name: checkout_steps.py
# Copyright 2015, Opex Software
# Apache License, Version 2.0
# This is a behave step-definitions file containing implementations of GWT's feature steps

import time
from behave import *
from features.pages.checkout_page import CheckoutPage

use_step_matcher("re")

@when('I add to cart the product (?:based on|number) (RUN_INDEX|\d+)')
def step(context,index):
    checkout = CheckoutPage(context.driver)
    checkout.add_product_to_cart(index)


@then('I proceed to checkout')
def step(context):
    checkout = CheckoutPage(context.driver)
    checkout.proceed_to_checkout.click()


@when('I select checkout method as Guest')
def step(context):
    checkout = CheckoutPage(context.driver)
    checkout.checkout_as_guest_radio.click()
    checkout.checkout_continue_button.click()


@when('I fill all mandatory details in Billing Information as (member|guest)')
def step(context,type):
    checkout = CheckoutPage(context.driver)
    checkout.fill_and_submit_billing_information(type)

@when('I continue with shipping method')
def step(context):
    checkout = CheckoutPage(context.driver)
    checkout.continue_with_shipping_method()

@when('I select payment method as "([^"]*)"')
def step(context,method):
    checkout = CheckoutPage(context.driver)
    if method == "check":
        checkout.payment_check.click()
    elif method == "cash_on_delivery":
        checkout.payment_cod.click()
    elif method == "credit_card":
        checkout.payment_cc.click()
        time.sleep(1)
        checkout.fill_credit_card_information()

    checkout.payment_continue_button.click()


@when('I place the order')
def step(context):
    checkout = CheckoutPage(context.driver)
    checkout.place_order_button.click()


@then('I should see order confirmation message')
def step(context):
    checkout = CheckoutPage(context.driver)
    checkout.verify_order_confirmation_message()