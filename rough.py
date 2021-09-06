import os
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
        EC.presence_of_element_located(
            (By.CLASS_NAME, "login_link")
        )
    )  
    print(f'The type of login is {type(login_page)}')

    # Clicks on the link taking us to the login page.
    login_page.click()  

    # Selects the username part of form.
    username_form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "id_auth-username")
        )
    )
    
    # Selects the password part of form.
    password_form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "id_auth-password")
        )
    )
    
    username = input('Entere your uername. ')
    password = input('Enter your password. ')

    username_form.send_keys(username)
    password_form.send_keys(password)
    
    # driver.quit()

except Exception as e:
    print('A problem has been encountered. ')
    print(e)
    driver.quit()

else:
    print('Code ran without any error.')



# Store password and usrname securely(probably as environemntal variables?).
# If environment variables are not found, then ask for username and password.