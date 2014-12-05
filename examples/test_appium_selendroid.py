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
from seleniumtid.test_cases import SeleniumTestCase
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from seleniumtid import selenium_driver


class AndroidEbookStore(SeleniumTestCase):
    def setUp(self):
        # Updating properties
        config = selenium_driver.config
        config.set('Browser', 'browser', 'android')
        config.set('AppiumCapabilities', 'automationName', 'Selendroid')
        config.set('AppiumCapabilities', 'platformName', 'Android')
        config.set('AppiumCapabilities', 'deviceName', 'Android Emulator')
        config.set('AppiumCapabilities', 'browserName', '')
        config.set('AppiumCapabilities', 'app', 'http://qacore02/sites/seleniumExamples/EbookStore.apk')
        config.set('AppiumCapabilities', 'appWaitActivity',
                   '.ui.activities.SplashViewActivity, .ui.activities.ListBookActivity')
        super(AndroidEbookStore, self).setUp()

    def test_open_book_by_title(self):
        book_title = "El Nombre de la Rosa"
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, book_title))).click()

        # Wait until page has changed
        self.utils.wait_until_element_not_visible((By.ID, "user_info"))

        opened_book_title = self.driver.find_element_by_id("titleView").text
        self.logger.debug("Book title: '" + opened_book_title + "'")
        self.assertEqual(book_title, opened_book_title, "The book title is wrong")
