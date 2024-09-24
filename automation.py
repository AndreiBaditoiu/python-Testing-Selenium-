import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('./chromedriver.exe')

chrome_browser = webdriver.Chrome(service=service)
chrome_browser.get('https://demoqa.com/automation-practice-form')
chrome_browser.maximize_window()
time.sleep(2)

assert 'DEMOQA' in chrome_browser.title
submit_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
print(submit_button.get_attribute('innerHTML'))

assert 'Submit' in chrome_browser.page_source
user_message = chrome_browser.find_element(By.ID, 'firstName')
user_message.clear()
user_message.send_keys('I am cool!')
chrome_browser.execute_script("arguments[0].scrollIntoView(true);", submit_button)
submit_button.click()
input("Press Enter to shot down...")
