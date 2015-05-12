# -*- coding: utf-8 -*-

u"""
(c) Copyright 2014 Telefónica, I+D. Printed in Spain (Europe). All Rights
Reserved.

The copyright to the software program(s) is property of Telefónica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefónica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
"""

import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from seleniumtid.test_cases import AppiumTestCase


class AndroidEbookStore(AppiumTestCase):
    def setUp(self):
        root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        config_file = os.path.join(root_path, 'conf', 'examples', 'properties.cfg')
        android_config_file = os.path.join(root_path, 'conf', 'examples', 'selendroid-ebook-properties.cfg')
        os.environ['Files_properties'] = '{};{}'.format(config_file, android_config_file)
        os.environ['Files_logging'] = os.path.join(root_path, 'conf', 'examples', 'logging.conf')
        os.environ['Files_output_path'] = os.path.join(root_path, 'dist')
        super(AndroidEbookStore, self).setUp()

    def test_open_book_by_title(self):
        book_title = "El Nombre de la Rosa"
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, book_title))).click()

        # Wait until page has changed
        self.utils.wait_until_element_not_visible((By.ID, "user_info"))

        opened_book_title = self.driver.find_element_by_id("titleView").text
        self.logger.debug("Book title: '" + opened_book_title + "'")
        self.assertEqual(book_title, opened_book_title, "The book title is wrong")
