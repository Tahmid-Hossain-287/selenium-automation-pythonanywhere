import os, time
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    driver = webdriver.Edge(r'./web_driver/msedgedriver.exe')
    actions = action_chains.ActionChains(driver)
    driver.set_window_size(1260, 905) # Resizes the window to a specific size.
    
except Exception as e:
    print('A problem occured while instantiating the driver ')
    print(e)

else:
    print('Driver instantiated successfully')


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

    else:
        print('Login page launched successfully')
        
# This function takes username and password and then logs in.
def login_with_credentials(username=None, password=None):
    if all([username, password]) is False:
        username = input("Please enter your username or email.")
        password = input("Please enter your password.")    



    try:
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

        # Writes the credentials required to login.
        username_form.send_keys(username)
        password_form.send_keys(password)
    
        # Identifies the login button of the web page.
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.ID, 'id_next')
            )
        ) 


        # Clicks the login button to login.
        login_button.click()

        


    except Exception as e:
        print('A problem was encountered at the login_with_credentials function. ')
        print(e)
        driver.quit()

    else:
        print('Successfully logged in')


def main():
    launch_login_page()
    login_with_credentials(os.getenv('pythonanywhere_username', default=None), os.getenv('pythonanywhere_password', default=None))


main()
