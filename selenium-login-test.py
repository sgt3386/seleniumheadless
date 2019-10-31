#!/usr/bin/env python
import time
import datetime
import pytz
import sys
from datetime import datetime
from pytz import timezone
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.support.ui import Select # Sllows selecting of visible page elements


#configure webdriver
print("Configuring WebDriver")
options = Options()
options.set_headless(headless=True)
caps = DesiredCapabilities.FIREFOX
caps['acceptInsecureCerts'] = True
pageload = DesiredCapabilities().FIREFOX
pageload["pageLoadStrategy"] = "normal" # Full complete
driver = webdriver.Firefox(capabilities=caps, firefox_options=options, desired_capabilities=pageload, executable_path='/home/ubuntu/geckodriver')
# predefined URLs
Test_Path_ = "[insert base URL here]"
login_URL_ = Test_Path_ + "[/login-path.jsp]"
Workspace_URL_ = Test_Path_ + "[/path to a workspace]"
logout_URL_ = Test_Path_ + "[/logout-path]"
screenshot_DIR = "/home/ubuntu/screenshots/"

print("Building functions")
def webpage_screenshot(page_content):
        # Takes a screenshot of the current headless state of firefox. page_content variable is a string for labeling
        date_format = '%Y%m%d-%H%M-%S'
        timestamp = datetime.now(tz=pytz.utc)
        timestamp = timestamp.astimezone(timezone('US/Pacific'))
        timestamp = (timestamp.strftime(date_format))
        screenshot_timestamp = "selenium-screenshot_" + page_content  + "_" + timestamp + ".png"
        screenshot_save = driver.save_screenshot(screenshot_DIR+screenshot_timestamp)
        print(screenshot_save)
        return

def webpage_login(URL):
        driver.get(URL)
        user = driver.find_element_by_name("user_name")
        password = driver.find_element_by_name("user_password")
        user.send_keys("[user.name]")
        password.send_keys("[pa55w0rd]")
        driver.find_element_by_name("Submit").click()
        print("Successful Login")
        return

def webpage_logout(URL):
        driver.get(URL)
        print("Successful Logout")
        return

def webpage_nav(URL):
        driver.get(URL)
        print(URL)
        return

def webpage_findtext(STRING):
        # Finds text in an element, returns TRUE/FALSE
        find_results = driver.find_element_by_xpath("//*[text()='" + STRING + "']")
        return

# Login to site
print("Attempting to login")
try:
        webpage_login(login_URL_)
except:
        sys.exit("ERROR: Cannot login")
        driver.close()
webpage_screenshot("login")

# Navigate KM
print("Attempting to navigate site")
try:
        webpage_nav(Workspace_URL_)
        time.sleep(15)
        webpage_findtext("Workspaces")
except:
        sys.exit("ERROR: Cannot navigate KM")
        driver.close()

webpage_screenshot("nav-to-workspace")

# Logout of KM
print("Logging out of test session")
try:
        webpage_logout(logout_URL_)
except:
        sys.exit("ERROR: Cannot logout of KM")
        driver.close()

webpage_screenshot("logout")
print("Testing concluded: Success")
driver.close()
