# selenium-automation-pythonanywhere
I have hosted an website on pythonanywhere. This project will click on the 'Run until 3 months from today' button on its own without me having to do it manually.

# How to make this work for you(If you use Edge)
Download the required version of web driver for edge and then put it in the '.\web_driver\' folder.

# How to make this work if you use browsers other than Edge
Make sure to download the rquired version of web driver for the browser of your choice. Place it in the '.\web_driver\' folder. Edit the driver variable accordingly.
For example, for chrome it will be:
driver = webdriver.Chrome(r'./web_driver/chromedriver.exe')


If you face any problems, make sure to create an issue.
