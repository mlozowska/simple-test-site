from tests.helpers.SupportFunctions import *

input_tab = 'inputs-header'
input_content = 'inputs-content'
input_field = '//*[@id="inputs-content"]/div/input'


def click_inputs_tab(driver_instance):
    elem = driver_instance.find_element_by_id(input_tab)
    elem.click()


def inputs_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, input_content)
    return elem.is_displayed()


def send_correct_keys_to_input(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, input_field)
    elem = driver_instance.find_element_by_xpath(input_field)
    elem.send_keys('123456')
    value = 123456
    if value == int(elem.get_attribute("value")):
        return True
    else:
        return False


def send_incorrect_keys_to_input(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, input_field)
    elem = driver_instance.find_element_by_xpath(input_field)
    elem.send_keys('abc')
    value = 'abc'
    if value == elem.get_attribute('value'):
        return False
    else:
        return True
