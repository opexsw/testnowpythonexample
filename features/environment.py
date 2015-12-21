import os
from selenium import webdriver

browser = os.getenv("BROWSER", "firefox")

def before_all(context):
    print("**************** " + browser + " **************")
    if browser == "chrome":
        context.driver=webdriver.Chrome()
        context.driver.maximize_window()
        context.driver.implicitly_wait(30)
        context.driver.set_page_load_timeout(120)
        context.driver.set_script_timeout(30)
    elif browser == "ie":
        print("A")
    else:
        context.driver=webdriver.Firefox()
        context.driver.maximize_window()
        context.driver.implicitly_wait(30)
        context.driver.set_page_load_timeout(120)
        context.driver.set_script_timeout(30)


def after_all(context):
    context.driver.quit()