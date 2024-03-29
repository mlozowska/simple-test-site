from tests.helpers.SupportFunctions import *
from requests import api

status_codes_header = 'statuscodes-header'
status_codes_content = 'statuscodes-content'
code_id_200 = '200siteAnchor'
code_id_305 = '305siteAnchor'
code_id_404 = '404siteAnchor'
code_id_500 = '500siteAnchor'


def status_code_tab(driver_instance):
    elem = driver_instance.find_element_by_id(status_codes_header)
    elem.click()


def status_code_content_visible(driver_instance):
    elem = wait_for_visibility_of_element_id(driver_instance, status_codes_content)
    return elem.is_displayed()


def code_200(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, code_id_200)
    status_200 = driver_instance.find_element_by_id(code_id_200)
    link_200 = status_200.get_attribute('href')
    r = api.get(link_200)
    if r.status_code == 200:
        return True
    else:
        return False


def code_305(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, code_id_305)
    code305 = driver_instance.find_element_by_id(code_id_305)
    link305 = code305.get_attribute('href')
    r = api.get(link305)
    if r.status_code == 305:
        return True
    else:
        return False


def code_404(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, code_id_404)
    code404 = driver_instance.find_element_by_id(code_id_404)
    link404 = code404.get_attribute('href')
    r = api.get(link404)
    if r.status_code == 404:
        return True
    else:
        return False


def code_500(driver_instance):
    wait_for_visibility_of_element_id(driver_instance, code_id_500)
    code500 = driver_instance.find_element_by_id(code_id_500)
    link500 = code500.get_attribute('href')
    r = api.get(link500)
    if r.status_code == 500:
        return True
    else:
        return False



