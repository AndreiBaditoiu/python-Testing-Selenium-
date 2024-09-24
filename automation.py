import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('./chromedriver.exe')

chrome_browser = webdriver.Chrome(service=service)
chrome_browser.get('https://www.google.com')
chrome_browser.maximize_window()
time.sleep(10)
chrome_browser.quit()


# print(chrome_browser)