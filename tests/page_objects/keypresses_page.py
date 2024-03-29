from tests.helpers.SupportFunctions import *
from selenium.webdriver.common.keys import Keys

key_presses_header = 'keypresses-header'
key_presses_content = 'keypresses-content'
key_presses_field = '//*[@id="target"]'
key_presses_result = '//*[@id="keyPressResult"]'


def click_key_presses_tab(driver_instance):
    wait_for_visibility_of_element_id(driver_instance,key_presses_header)
    elem = driver_instance.find_element_by_id(key_presses_header)
    elem.click()


def key_presses_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, key_presses_content)
    return elem.is_displayed()


def enter_key_press(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, key_presses_field)
    elem = driver_instance.find_element_by_xpath(key_presses_field)
    elem.send_keys(Keys.RETURN)
    info = driver_instance.find_element_by_xpath(key_presses_result)
    message = "You entered: ENTER"
    if message == info.text:
        return True
    else:
        return False


def letter_key_press(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, key_presses_field)
    elem = driver_instance.find_element_by_xpath(key_presses_field)
    elem.send_keys("a")
    info = driver_instance.find_element_by_xpath(key_presses_result)
    message = "You entered: A"
    if message == info.text:
        return True
    else:
        return False


