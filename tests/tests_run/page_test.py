import unittest
from selenium import webdriver

from config.test_settings import TestSettings
from tests.page_objects import main_page, checkboxes_page, hovers_page, users_page,\
    input_page, dropdown_page, add_remove_page, data_picker_page, basic_auth_page, logged_in_page, \
    form_page, keypresses_page


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:/Program Files/chromedriver/chromedriver.exe")
        self.url = TestSettings.page_url
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_main_page_content_visible(self):
        self.assertTrue(main_page.content_visible(self.driver))

    def test_checkboxes(self):
        checkboxes_page.click_checkboxes_tab(self.driver)
        self.assertTrue(checkboxes_page.checkboxes_visible(self.driver))
        checkboxes_page.click_checkboxes(self.driver)

    def test_hovers(self):
        hovers_page.click_hovers_tab(self.driver)
        self.assertTrue(hovers_page.hover_content_displayed(self.driver))
        hovers_page.hover_over_element_and_click(self.driver)
        self.assertTrue(users_page.error_info_displayed(self.driver))

    def test_inputs_visibility(self):
        input_page.click_inputs_tab(self.driver)
        self.assertTrue(input_page.inputs_content_visible(self.driver))

    def test_inputs_correct_input(self):
        input_page.click_inputs_tab(self.driver)
        self.assertTrue(input_page.send_correct_keys_to_input(self.driver))

    def test_inputs_incorrect_input(self):
        input_page.click_inputs_tab(self.driver)
        self.assertTrue(input_page.send_incorrect_keys_to_input(self.driver))

    def test_dropdown_select(self):
        dropdown_page.click_dropdown_tab(self.driver)
        self.assertTrue(dropdown_page.dropdown_content_visible(self.driver))
        dropdown_page.get_first_dropdown_value(self.driver)

    def test_add_element(self):
        add_remove_page.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_element_content(self.driver))
        add_remove_page.add_element(self.driver)

    def test_delete_element(self):
        # you can use the previous function
        # Tests.test_add_element(self)

        add_remove_page.click_add_remove_tab(self.driver)
        self.assertTrue(add_remove_page.add_remove_element_content(self.driver))
        add_remove_page.add_element(self.driver)
        add_remove_page.delete_element(self.driver)
        self.assertTrue(add_remove_page.element_invisible(self.driver))

    def test_date_picker_tab_select(self):
        data_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(data_picker_page.date_picker_content_visible(self.driver))

    def test_date_visible(self):
        data_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(data_picker_page.correct_date_visible(self.driver))

    def test_send_correct_date(self):
        data_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(data_picker_page.correct_date_visible(self.driver))
        data_picker_page.send_correct_date(self.driver)

    def test_send_incorrect_date(self):
        data_picker_page.click_date_picker_tab(self.driver)
        self.assertTrue(data_picker_page.correct_date_visible(self.driver))
        data_picker_page.send_incorrect_date(self.driver)

    # Basic auth tests
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

    # Logged in tests
    def test_logged_in_info_visible(self):
        basic_auth_page.click_basic_auth_header(self.driver)
        self.assertTrue(basic_auth_page.basic_auth_content_visible(self.driver))
        basic_auth_page.send_correct_data(self.driver)
        self.assertTrue(logged_in_page.logged_in_info_displayed(self.driver))

    def test_return_to_main_page(self):
        Tests.test_logged_in_info_visible(self)
        logged_in_page.click_return_button(self.driver)
        self.assertTrue(main_page.content_visible(self.driver))

    # Form page tests
    def test_form_page_content_visible(self):
        form_page.click_form_page_header(self.driver)
        self.assertTrue(form_page.form_content_visible(self.driver))

    def test_send_correct_data(self):
        form_page.click_form_page_header(self.driver)
        self.assertTrue(form_page.send_first_last_names(self.driver))

    # Key presses page tests
    def test_click_enter(self):
        keypresses_page.click_key_presses_tab(self.driver)
        self.assertTrue(keypresses_page.key_presses_content_visible(self.driver))

    def test_info_enter_visible(self):
        keypresses_page.click_key_presses_tab(self.driver)
        self.assertTrue(keypresses_page.key_presses_content_visible(self.driver))
        keypresses_page.enter_key_press(self.driver)
        self.assertTrue(keypresses_page.enter_info_visible(self.driver))



if __name__ == '__main__':
    unittest.main()