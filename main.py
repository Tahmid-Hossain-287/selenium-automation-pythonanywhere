import os
from selenium import webdriver

driver = webdriver.Edge(r'./web_driver/msedgedriver.exe')

driver.get('https://www.pythonanywhere.com')
print('done')
