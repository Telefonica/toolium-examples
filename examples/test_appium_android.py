# -*- coding: utf-8 -*-
'''
(c) Copyright 2014 Telefonica, I+D. Printed in Spain (Europe). All Rights
Reserved.

The copyright to the software program(s) is property of Telefonica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefonica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
'''
from seleniumtid.test_cases import AppiumTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from seleniumtid import selenium_driver
from seleniumtid.config_driver import ConfigDriver
from examples.pageobjects.register import RegisterPageObject
import os


class AndroidEbookStore(AppiumTestCase):
    def setUp(self):
        root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        config_file = os.path.join(root_path, 'conf', 'examples', 'properties.cfg')
        android_config_file = os.path.join(root_path, 'conf', 'examples', 'android-ebook-properties.cfg')
        os.environ['Files_properties'] = '{};{}'.format(config_file, android_config_file)
        os.environ['Files_logging'] = os.path.join(root_path, 'conf', 'examples', 'logging.conf')
        super(AndroidEbookStore, self).setUp()

    def test_open_book_by_title(self):
        book_title = "El Nombre de la Rosa"
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, book_title))).click()

        # Wait until page has changed
        self.utils.wait_until_element_not_visible((By.ID, "com.tdigital.ebookstore:id/user_info"))

        opened_book_title = self.driver.find_element_by_id("com.tdigital.ebookstore:id/titleView").text
        self.logger.debug("Book title: '" + opened_book_title + "'")
        self.assertEqual(book_title, opened_book_title, "The book title is wrong")

    def test_mobile_and_browser(self):
        # Create a second driver
        config = selenium_driver.config.deepcopy()
        config.set('Browser', 'browser', 'firefox')
        firefoxdriver = ConfigDriver(config).create_driver()
        self.addCleanup(firefoxdriver.quit)

        # Mobile: open book
        book_title = "El Nombre de la Rosa"
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.NAME, book_title))).click()

        # Web: register user
        user = {'username': 'user1', 'password': 'pass1', 'name': 'name1', 'email': 'user1@mailinator.com',
                'place': 'Barcelona'}
        register_page = RegisterPageObject(firefoxdriver)
        register_page.open()
        register_page.register(user)
