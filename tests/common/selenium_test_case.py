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
import unittest
import logging
from selenium_python import selenium_driver


class SeleniumTestCase(unittest.TestCase):
    def get_subclassmethod_name(self):
        return self.__class__.__name__ + "." + self._testMethodName

    def setUp(self):
        # Configure logger
        self.logger = logging.getLogger(__name__)
        # Create driver
        self.driver = selenium_driver.connect()
        # Maximize browser
        if not selenium_driver.is_mobile_test():
            self.driver.maximize_window()
        self.logger.info("Running new test: {0}".format(self.get_subclassmethod_name()))

    def tearDown(self):
        # Close browser and stop driver
        self.driver.quit()
