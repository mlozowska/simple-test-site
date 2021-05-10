from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def hover_over_element(driver_instance, element):
    hover = ActionChains(driver_instance).move_to_element(element)
    hover.perform()


def wait_for_visibility_of_element_xpath(driver_instance, xpath):
    try:
        elem = WebDriverWait(driver_instance, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    except TimeoutException:
        elem = False
    return elem


def wait_for_visibility_of_element_id(driver_instance, id):
    try:
        elem = WebDriverWait(driver_instance, 10).until(EC.visibility_of_element_located((By.ID, id)))
    except TimeoutException:
        elem = False
    return elem


# def wait_for_invisibility_of_element_xpath(inv_driver_instance, xpath):
#     try:
#         inv_elem = WebDriverWait(inv_driver_instance, 10).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
#     except TimeoutException:
#         inv_elem = False
#     return inv_elem


def wait_for_invisibility_of_element_xpath(inv_driver_instance, xpath):
    inv_element = WebDriverWait(inv_driver_instance, 8).until(EC.invisibility_of_element_located((By.XPATH, xpath)))
    return inv_element