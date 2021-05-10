"""
An explicit wait makes WebDriver wait for a certain condition to occur before proceeding further with execution.
Allows you to set the time that the condition has to be satisfied before it returns a timeout exception.
Better - more control, less risk
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:/Program Files/chromedriver/chromedriver.exe")
driver.get('http://simpletestsite.fabrykatestow.pl/')
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkbox-header"))
    )
finally:
    driver.quit()