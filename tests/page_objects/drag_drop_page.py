from tests.helpers.SupportFunctions import *
import os

drag_drop_header = 'draganddrop-header'
drag_drop_content = 'draganddrop-content'
elem_a = '//*[@id="column-a"]'
elem_b = '//*[@id="column-b"]'


def click_drag_drop_tab(driver_instance):
    elem = driver_instance.find_element_by_id(drag_drop_header)
    elem.click()


def drag_drop_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, drag_drop_content)
    return elem.is_displayed()


def drag_drop_element(driver_instance):
    with open(os.path.abspath('drag_and_drop_helper.js'), 'r') as js_file:
        line = js_file.readline()
        script = ''
        while line:
            script += line
            line = js_file.readline()

    driver_instance.execute_script(script + "jQuery('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")
    return True








