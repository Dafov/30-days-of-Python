import time
from selenium import webdriver

browser = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')

url = 'https://google.com'
browser.get(url)

"""
<input type='text' class='' id='' name='??' />
<textarea name='??'><textarea>
<input name="q" type="text">
"""
time.sleep(2)
name = 'q'
search_el = browser.find_element_by_name("q")
# print(search_el)
# search_el = browser.find_elements_by_css_selector("h1")
search_el.send_keys("selenium python")

accept_btn_class = "jyfHyd"
accept_btn = browser.find_element_by_class_name(accept_btn_class)
time.sleep(1)
accept_btn.click()

confirm_btn_class = "VfPpkd-dgl2Hf-ppHlrf-sM5MNb"
confirm_btn = browser.find_element_by_class_name(confirm_btn_class)
time.sleep(1)
confirm_btn.click()
"""
<input type='submit' />
<button type='submit' />
<form></form>
<input type="submit">
"""
submit_btn_el = browser.find_element_by_css_selector("input[type='submit']")
# print(submit_btn_el.get_attribute('name'))
time.sleep(2)
submit_btn_el.click()