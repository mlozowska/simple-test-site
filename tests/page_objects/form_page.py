from tests.helpers.SupportFunctions import *
from selenium.webdriver.common.alert import Alert

form_page_tab = 'form-header'
form_content = 'form-content'
first_name_field = 'fname'
last_name_field = 'lname'
first_name = 'Marie'
last_name = 'Curie'
submit_button = '//*[@id="formSubmitButton"]'


def click_form_page_header(driver_instance):
    elem = driver_instance.find_element_by_id(form_page_tab)
    elem.click()


def form_content_visible(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, form_content)
    elem = driver_instance.find_element_by_id(form_content)
    return elem.is_displayed()


def send_first_last_names(driver_instance):
    f_name = driver_instance.find_element_by_id(first_name_field)
    f_name.send_keys(first_name)
    l_name = driver_instance.find_element_by_id(last_name_field)
    l_name.send_keys(last_name)
    sub_button = driver_instance.find_element_by_xpath(submit_button)
    sub_button.click()
    alert = Alert(driver_instance)
    value = "success"
    if value == alert.text:
        return True
    else:
        return False

