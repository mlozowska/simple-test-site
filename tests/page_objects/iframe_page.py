from tests.helpers.SupportFunctions import *

iframe_tab = 'iframe-header'
iframe_content = 'iframe-content'
iframe_area = 'iframe'
button_1 = 'simpleButton1'
button_2 = 'simpleButton2'
notification = 'whichButtonIsClickedMessage'


def click_iframe_tab(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, iframe_tab)
    elem = driver_instance.find_element_by_id(iframe_tab)
    elem.click()


def iframe_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, iframe_content)
    return elem.is_displayed()


def click_inside_iframe_one(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, iframe_area)
    driver_instance.switch_to.frame(driver_instance.find_element_by_tag_name("iframe"))
    driver_instance.find_element_by_id(button_1).click()
    result = driver_instance.find_element_by_id(notification).text
    if result == 'Button 1 was clicked!':
        return True
    else:
        return False


def click_inside_iframe_two(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, iframe_area)
    driver_instance.switch_to.frame(driver_instance.find_element_by_tag_name("iframe"))
    driver_instance.find_element_by_id(button_2).click()
    result = driver_instance.find_element_by_id(notification).text
    if result == 'Button 2 was clicked!':
        return True
    else:
        return False

