from tests.helpers.SupportFunctions import *
from selenium.webdriver.support.select import Select

dropdown_tab = 'dropdownlist-header'
dropdown_content = 'dropdownlist-content'
dropdown_list = 'dropdown'


def click_dropdown_tab(driver_instance):
    elem = driver_instance.find_element_by_id(dropdown_tab)
    elem.click()


def dropdown_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, dropdown_content)
    return elem.is_displayed()


def get_first_dropdown_value(driver_instance):
    # use Select to for dropdown list
    elem_list = Select(driver_instance.find_element_by_id(dropdown_list))
    wait_for_visibility_of_element_id(driver_instance, dropdown_list)
    # user select_by_index method to get to 'Option 1'
    elem_list.select_by_index(1)

