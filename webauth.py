from selenium import webdriver
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
browser.get('http://github.com')

sign_in_link=browser.find_element(By.LINK_TEXT,'Sign in')
sign_in_link.click()

# username_box=browser.find_element_by_id('login_filed')
# username_box.setkey('preshy')

# password_link=browser.find_element_by_id('login_filed')
# password_link.setkey('nice')
# password_link.submit()

# assert 'preshy' in browser.page_source