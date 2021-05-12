from tests.helpers.SupportFunctions import *

drag_drop_header = 'draganddrop-header'
drag_drop_content = 'draganddrop-content'
elem_a = 'column-a'
elem_b = 'column-b'


def click_drag_drop_tab(driver_instance):
    elem = driver_instance.find_element_by_id(drag_drop_content)
    elem.click()


def drag_drop_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, drag_drop_content)
    return elem.is_displayed()

def drag_drop_element_a(driver_instance):
    drag_and_drop_by_id(driver_instance, driver_instance.find_element_by_id(elem_a)
    elem = driver_instance.find_element_by_id(elem_b)
    elem.click()







