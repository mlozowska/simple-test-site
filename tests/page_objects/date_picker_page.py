from tests.helpers.SupportFunctions import *


date_picker_tab = 'datepicker-header'
date_picker_content = 'datepicker-content'
date_picker_field = '//*[@id="start"]'


def click_date_picker_tab(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, date_picker_tab)
    elem = driver_instance.find_element_by_id(date_picker_tab)
    elem.click()


def date_picker_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, date_picker_content)
    return elem.is_displayed()


def click_date_picker_field(driver_instance):
    elem = driver_instance.find_element_by_id(date_picker_field)
    elem.click()


def correct_date_visible(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, date_picker_field)
    elem = driver_instance.find_element_by_xpath(date_picker_field)
    value = '2020-07-22'
    if value == str(elem.get_attribute("value")):
        return True
    else:
        return False


def send_correct_date(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, date_picker_field)
    element = driver_instance.find_element_by_xpath(date_picker_field)
    picked_date = "2020-02-21"
    element.send_keys(picked_date)
    if picked_date == element.get_attribute("value"):
        return True
    else:
        return False


def send_incorrect_date(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, date_picker_field)
    elem = driver_instance.find_element_by_xpath(date_picker_field)
    picked_date = "abc-05-10"
    elem.send_keys(picked_date)
    if picked_date == elem.get_attribute("value"):
        return False
    else:
        return True



