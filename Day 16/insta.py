# import getpass
# my_password = getpass.getpass("What is your password?\n")
# print(my_password)

import time
from conf import INSTA_USERNAME, INSTA_PASSWORD
from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')

url = "https://www.instagram.com"
browser.get(url)

time.sleep(2)
accept_btn_xpath = "/html/body/div[2]/div/div/button[1]"
accept_btn = browser.find_element_by_xpath(accept_btn_xpath)
# print(accept_btn)
accept_btn.click()

time.sleep(2)
username_el = browser.find_element_by_name("username")
username_el.send_keys(INSTA_USERNAME)

password_el = browser.find_element_by_name("password")
password_el.send_keys(INSTA_PASSWORD)

time.sleep(1.5)
submit_btn_el = browser.find_element_by_css_selector("button[type='submit']")
submit_btn_el.click()

