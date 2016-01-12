import os
from selenium import webdriver
import selenium.webdriver.chrome.service

browser = os.getenv("BROWSER", "firefox")
har = os.getenv("IS_UPA", "false")


def before_all(context):
    print("**************** " + browser + " **************")
    if browser == "chrome":
        context.driver=webdriver.Chrome()
        context.driver.maximize_window()
        context.driver.implicitly_wait(30)
        context.driver.set_page_load_timeout(120)
        context.driver.set_script_timeout(30)
    elif browser == "ie":
        caps = webdriver.DesiredCapabilities.INTERNETEXPLORER
        caps['javascript_enabled'] = True
        caps['native_events'] = False
        caps['acceptSslCerts'] = True
        context.driver = webdriver.Ie(caps)
        context.driver.maximize_window()
        context.driver.implicitly_wait(30)
        context.driver.set_page_load_timeout(120)
        context.driver.set_script_timeout(30)
    elif browser == "opera":
        print "A"
    else:
        if har == "true":
            profile = webdriver.FirefoxProfile()
            profile.add_extension(extension="data/har/firebug-2.0.13.xpi")
            profile.add_extension(extension="data/har/netExport-0.8.xpi")
            profile.set_preference("extensions.firebug.currentVersion", "2.0.13")
            profile.set_preference("extensions.firebug.allPagesActivation","on")
            profile.set_preference("extensions.firebug.defaultPanelName","net")
            profile.set_preference("extensions.firebug.net.enableSites","true")
            profile.set_preference("extensions.firebug.netexport.alwaysEnableAutoExport","true")
            profile.set_preference("extensions.firebug.netexport.defaultLogDir",os.path.abspath("reports/har"))
            context.driver=webdriver.Firefox(firefox_profile=profile)
        else:
            context.driver=webdriver.Firefox()

        context.driver.maximize_window()
        context.driver.implicitly_wait(30)
        context.driver.set_page_load_timeout(120)
        context.driver.set_script_timeout(30)

def before_scenario(context,scenario):
    context.driver.delete_all_cookies()

def after_all(context):
    context.driver.quit()