# -*- coding: utf-8 -*-
'''
(c) Copyright 2015 Telefonica, I+D. Printed in Spain (Europe). All Rights
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
import os


class IosTestApp(AppiumTestCase):
    def setUp(self):
        root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        config_file = os.path.join(root_path, 'conf', 'examples', 'properties.cfg')
        ios_config_file = os.path.join(root_path, 'conf', 'examples', 'ios-properties.cfg')
        os.environ['Files_properties'] = '{};{}'.format(config_file, ios_config_file)
        os.environ['Files_logging'] = os.path.join(root_path, 'conf', 'examples', 'logging.conf')
        super(IosTestApp, self).setUp()

    def test_sum(self):
        first_number = 2
        second_number = 3

        first_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "TextField1")))
        first_element.send_keys(first_number)
        self.driver.find_element_by_name("TextField2").send_keys(second_number)
        self.driver.find_element_by_accessibility_id("ComputeSumButton").click()
        result = int(self.driver.find_element_by_xpath("//UIAStaticText[1]").text)
        self.logger.debug("{} + {} = {}".format(first_number, second_number, result))
        self.assertEqual(first_number + second_number, result, "Wrong sum")
