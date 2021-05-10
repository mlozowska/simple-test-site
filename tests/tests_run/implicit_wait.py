"""
An implicit wait makes WebDriver poll the DOM for a certain amount of time when trying to locate an element.
Sets the global time that the WebDriver object has to find an item before it returns an exception that the item is missing.
By default, it is set to 0.
"""

from selenium import webdriver

driver = webdriver.Chrome("C:/Program Files/chromedriver/chromedriver.exe")
driver.implicitly_wait(10)
driver.get('http://simpletestsite.fabrykatestow.pl/')
myDynamicElement = driver.find_element_by_id("checkbox-header")
driver.quit()
