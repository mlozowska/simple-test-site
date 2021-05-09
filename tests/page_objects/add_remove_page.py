from tests.helpers.SupportFunctions import *

add_remove_elements_header = 'addremoveelements-header'
add_remove_elements_content = 'addremoveelements-content'
add_element_button = '//*[@id="addremoveelements-content"]/div/div/button'
delete_button = '//*[@id="elements"]/button'


def click_add_remove_tab(driver_instance):
    elem = driver_instance.find_element_by_id(add_remove_elements_header)
    elem.click()


def add_remove_element_content(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, add_remove_elements_header)
    return elem.is_displayed()


def add_element(driver_instance):
    elem = driver_instance.find_element_by_xpath(add_element_button)
    elem.click()


def delete_element(driver_instance):
    elem = driver_instance.find_element_by_xpath(delete_button)
    elem.click()
    wait_for_invisibility_of_element_xpath(driver_instance, delete_button)


def element_invisible(driver_instance):
    try:
        wait_for_invisibility_of_element_xpath(driver_instance, delete_button)
        return True
    except NoSuchElementException:
        return False

