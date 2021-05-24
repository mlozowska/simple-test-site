import unittest
from selenium import webdriver

from config.test_settings import TestSettings
from tests.page_objects import add_remove_page, logged_in_page, \
    keypresses_page, drag_drop_page, status_codes_page
from tests.page_objects import hovers_page, form_page, dropdown_page, users_page, checkboxes_page, main_page, \
    input_page, basic_auth_page, iframe_page, date_picker_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Program Files/chromedriver/chromedriver.exe")
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    # Main page Test
    def test_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    # Checkboxes page Test
    def test_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)

    # Hovers page Test
    def test_hovers(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hover_content_displayed(self.driver))
        hovers_page.hover_over_element_and_click(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    # Inputs page Tests
    def test_inputs_visibility(self):
        input_page.click_inputs_tab(self.driver)
        self.assertTrue(input_page.inputs_content_visible(self.driver))

    def test_inputs_correct_input(self):
        input_page.click_inputs_tab(self.driver)
        self.assertTrue(input_page.send_correct_keys_to_input(self.driver))

    def test_inputs_incorrect_input(self):
        input_page.click_inputs_tab(self.driver)
        self.assertTrue(input_page.send_incorrect_keys_to_input(self.driver))

    # Drop-down page Test
    def test_dropdown_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_visible(self.driver))
        dropdown_page.get_first_dropdown_value(self.driver)

    # Add/remove elements page Test
    def test_add_element(self):
        add_remove_page.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_element_content(self.driver))
        add_remove_page.add_element(self.driver)

    def test_delete_element(self):
        add_remove_page.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_element_content(self.driver))
        add_remove_page.add_element(self.driver)
        add_remove_page.delete_element(self.driver)
        self.assertTrue(add_remove_page.element_invisible(self.driver))

    # Date picker page Tests
    def test_date_visible(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.correct_date_visible(self.driver))

    def test_send_correct_date(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.send_correct_date(self.driver))

    def test_send_incorrect_date(self):
        date_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(date_picker_page.send_incorrect_date(self.driver))

    # Basic auth page Tests
    def test_basic_auth_content_visible(self):
        basic_auth_page.click_basic_auth_header(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))

    def test_incorrect_credentials_visible(self):
        basic_auth_page.click_basic_auth_header(self.driver)
        self.assertTrue(basic_auth_page.invalid_credentials_displayed(self.driver))

    def test_correct_credentials(self):
        basic_auth_page.click_basic_auth_header(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        basic_auth_page.send_correct_data(self.driver)

    # Logged in page Tests
    def test_logged_in_info_visible(self):
        basic_auth_page.click_basic_auth_header(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        basic_auth_page.send_correct_data(self.driver)
        self.assertTrue(logged_in_page.logged_in_info_displayed(self.driver))

    def test_return_to_main_page(self):
        Tests.test_logged_in_info_visible(self)
        logged_in_page.click_return_button(self.driver)
        self.assertTrue(main_page.content_visible(self.driver))

    # Form page Tests
    def test_form_page_content_visible(self):
        form_page.click_form_page_header(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))

    def test_send_correct_data(self):
        form_page.click_form_page_header(self.driver)
        self.assertTrue(form_page.send_first_last_names(self.driver))

    # Key presses page Tests
    def test_click_enter(self):
        keypresses_page.click_key_presses_tab(self.driver)
        self.assertTrue(keypresses_page.key_presses_content_visible(self.driver))

    def test_info_enter_visible(self):
        keypresses_page.click_key_presses_tab(self.driver)
        self.assertTrue(keypresses_page.key_presses_content_visible(self.driver))
        keypresses_page.enter_key_press(self.driver)
        self.assertTrue(keypresses_page.enter_info_visible(self.driver))

    # Status code page Tests
    def test_status_codes_visible(self):
        status_codes_page.status_code_tab(self.driver)
        self.assertTrue(status_codes_page.status_code_content_visible(self.driver))

    def test_status_code_displayed_200(self):
        status_codes_page.status_code_tab(self.driver)
        self.assertTrue(status_codes_page.code_200(self.driver))

    # IFrame page Tests
    def test_iframe_content_visible(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.iframe_content_visible(self.driver))

    def test_iframe_1(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.click_inside_iframe_one(self.driver))

    def test_iframe_2(self):
        iframe_page.click_iframe_tab(self.driver)
        self.assertTrue(iframe_page.click_inside_iframe_two(self.driver))

    # Drag and drop page Tests
    def test_drag_drop_content_visible(self):
        drag_drop_page.click_drag_drop_tab(self.driver)
        self.assertTrue(drag_drop_page.drag_drop_content_visible(self.driver))

    def test_drag_and_drop_element(self):
        drag_drop_page.click_drag_drop_tab(self.driver)
        self.assertTrue(drag_drop_page.drag_drop_element(self.driver))



if __name__ == '__main__':
    unittest.main()