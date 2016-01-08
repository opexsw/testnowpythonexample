# Name =  dashboard_page.py
# Copyright 2015, Opex Software
# Apache License, Version 2.0
# This is a page object file for Magento Checkout page containing web-elements and its interactive methods


from page_objects import PageObject, PageElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

class DashboardPage(PageObject):

    search_box = PageElement(id_ = "search")
    search_button = PageElement(xpath = "//button[@title='Search']")
    product_catalog = PageElement(css = "div.category-products")
    save_button = PageElement(xpath = "//button[@title='Save']")
    general_subscription_checkbox = PageElement(id_ = "subscription")
    success_message = PageElement(css = "li.success-msg span")
    newsletter_subscription_textbox = PageElement(id_ = "newsletter")
    subscribe_button = PageElement(xpath = "//button[@title='Subscribe']")

    def __init__(self,driver):
       super(DashboardPage,self).__init__(driver)
       self.driver = driver


    def do_a_global_search(self,keyword):
        self.search_box = keyword
        self.search_button.click()


    def wait_for_products_to_be_displayed(self):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.category-products")))


    def general_subscription(self,action):
        if action == "select":
            if not self.general_subscription_checkbox.is_selected():
            # if not self.driver.find_element(By.ID,"subscription").is_selected():
                self.general_subscription_checkbox.click()
        elif action == "de-select":
            if self.driver.find_element(By.ID,"subscription").is_selected():
                self.general_subscription_checkbox.click()


    def enter_newsletter_email(self,fresh_or_used):
        faker = Faker()
        if fresh_or_used == "fresh":
            self.newsletter_subscription_textbox = faker.email()
        elif fresh_or_used == "registered":
            self.newsletter_subscription_textbox = "admin@mailinator.com"

