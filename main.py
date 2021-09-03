import os, time
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge(r'./web_driver/msedgedriver.exe')

driver.get('https://www.pythonanywhere.com')
actions = action_chains.ActionChains(driver)


try:
    # Finds the link that takes to the login page.
    login_page = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "login_link"))
    )  
    print(f'The type of login is {type(login)}')

    # Clicks on the link taking us to the login page.
    login_page.click()  
    
    
    
    # driver.quit()

except Exception as e:
    print(e)
    driver.quit()