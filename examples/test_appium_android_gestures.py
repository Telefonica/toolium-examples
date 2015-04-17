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
from appium.webdriver.common.touch_action import TouchAction
import os


class AndroidGestures(AppiumTestCase):
    def setUp(self):
        root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        config_file = os.path.join(root_path, 'conf', 'examples', 'properties.cfg')
        android_config_file = os.path.join(root_path, 'conf', 'examples', 'android-apidemos-properties.cfg')
        os.environ['Files_properties'] = '{};{}'.format(config_file, android_config_file)
        os.environ['Files_logging'] = os.path.join(root_path, 'conf', 'examples', 'logging.conf')
        super(AndroidGestures, self).setUp()

    def test_drag_and_drop(self):
        scrolled_locator = 'new UiScrollable(new UiSelector().scrollable(true).instance(0))' \
                           '.scrollIntoView(new UiSelector().text("{}").instance(0));'
        self.driver.find_element_by_android_uiautomator(scrolled_locator.format('Views')).click()
        self.driver.find_element_by_android_uiautomator(scrolled_locator.format('Drag and Drop')).click()

        # Drag and drop an element
        dd3 = self.driver.find_element_by_id('com.example.android.apis:id/drag_dot_3')
        dd2 = self.driver.find_element_by_id('com.example.android.apis:id/drag_dot_2')
        # dnd is stimulated by longpress-move_to-release
        TouchAction(self.driver).long_press(dd3).move_to(dd2).release().perform()

        # Check movement
        el = self.driver.find_element_by_id('com.example.android.apis:id/drag_result_text')
        self.assertEqual('Dropped!', el.get_attribute('text'))
