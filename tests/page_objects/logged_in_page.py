from tests.helpers.SupportFunctions import *

logged_in_message = '//*[@id="loggedInMessage"]'
return_button = '//*[@id="retrun button"]'


def logged_in_info_displayed(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, logged_in_message)
    elem = driver_instance.find_element_by_xpath(logged_in_message)
    info_msg = "You are logged in!"
    if info_msg == elem.text:
        return True
    else:
        return False


def click_return_button(driver_instance):
    elem = driver_instance.find_element_by_xpath(return_button)
    elem.click()