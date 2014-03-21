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
from selenium_tid_python.selenium_test_case import SeleniumTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium_tid_python import selenium_driver


class AndroidEbookStore(SeleniumTestCase):
    def setUp(self):
        # Updating properties
        config = selenium_driver.config
        self.previous_browser = config.get('Browser', 'browser')
        if not config.getboolean_optional('Server', 'enabled'):
            config.set('Browser', 'browser', 'android')
        config.set('AppiumCapabilities', 'device', 'android')
        config.set('AppiumCapabilities', 'app', 'http://qacore02/sites/seleniumExamples/EbookStore.apk')
        config.set('AppiumCapabilities', 'app-package', 'com.tdigital.ebookstore')
        config.set('AppiumCapabilities', 'app-activity', '.ui.activities.SplashViewActivity')
        super(AndroidEbookStore, self).setUp()

    def tearDown(self):
        # Updating properties to previous values
        super(AndroidEbookStore, self).tearDown()
        config = selenium_driver.config
        config.set('Browser', 'browser', self.previous_browser)

    def test_open_book_by_title(self):
        book_title = "El Nombre de la Rosa"
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable((By.NAME, book_title))).click()
        opened_book_title = self.driver.find_element_by_xpath("//TextView[2]").text
        self.logger.debug("Book title: '" + opened_book_title + "'")
        self.assertEqual(book_title, opened_book_title, "The book title is wrong")
