import time
import config as cfg
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException

passwd = cfg.passwd
opts = Options()
opts.headless = True

browser = webdriver.Firefox(options=opts)
browser.get("https://wireless.mvcc.edu")

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")
submit   = browser.find_element_by_name("Submit")

username.send_keys("<login username>")
password.send_keys(passwd)

submit.click()

wait = WebDriverWait( browser, 5 )

try:
    page_loaded = wait.until_not(
            lambda browser: browser.current_url == "https://wireless.mvcc.edu"
            )
except TimeoutException:
    print("Loading Timeout Expired...")
    browser.quit()
    quit()

print("Login-in Successful")
browser.quit()
quit()
