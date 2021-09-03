import os, time
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge(r'./web_driver/msedgedriver.exe')
actions = action_chains.ActionChains(driver)


def launch_login_page():
    # This function launches the login page of pythonanywhere.com website.
    try:
        driver.get('https://www.pythonanywhere.com')
        
        # Finds the link that takes to the login page.
        login_page =  WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "login_link")
            )
        )

        # Clicks on the link taking us to the login page.
        login_page.click()  	

    except Exception as e:
        print('A problem occured at launch_login_page funciton.')
        print(e)
        driver.quit()



launch_login_page()