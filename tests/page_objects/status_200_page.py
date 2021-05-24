from tests.helpers.SupportFunctions import *

status_200 = '/html/body/pre'


def status_code_200_displayed(driver_instance):
    elem = wait_for_visibility_of_element_xpath(driver_instance, status_200)
    # elem = driver_instance.find_element_by_xpath(status_200)
    return elem.is_displayed()