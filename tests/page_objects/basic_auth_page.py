from tests.helpers.SupportFunctions import *

basic_auth_tab = 'basicauth-header'
basic_auth_content = 'basicauth-content'
username_field = '//*[@id="ba_username"]'
password_field = '//*[@id="ba_password"]'
login_field = '//*[@id="content"]/button'
invalid_credentials_info = '//*[@id="loginFormMessage"]'


def click_basic_auth_header(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, basic_auth_tab)
    elem = driver_instance.find_element_by_id(basic_auth_tab)
    elem.click()


def basic_auth_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, basic_auth_content)
    return elem.is_displayed()


def send_correct_data(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, username_field)
    elem1 = driver_instance.find_element_by_xpath(username_field)
    elem1.send_keys('admin')
    elem2 = driver_instance.find_element_by_xpath(password_field)
    elem2.send_keys('admin')
    elem3 = driver_instance.find_element_by_xpath(login_field)
    elem3.click()


def send_invalid_data(driver_instance):
    wait_for_visibility_of_element_xpath(driver_instance, username_field)
    elem1 = driver_instance.find_element_by_xpath(username_field)
    elem1.send_keys('abc')
    elem2 = driver_instance.find_element_by_xpath(password_field)
    elem2.send_keys('123')
    elem3 = driver_instance.find_element_by_xpath(login_field)
    elem3.click()
    wait_for_visibility_of_element_xpath(driver_instance, invalid_credentials_info)
    elem = driver_instance.find_element_by_xpath(invalid_credentials_info)
    info_msg = "Invalid credentials"
    if info_msg == elem.text:
        return True
    else:
        return False



