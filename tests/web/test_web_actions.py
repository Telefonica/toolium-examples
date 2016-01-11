# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from nose.tools import assert_equal
from selenium.webdriver.common.action_chains import ActionChains, Keys

from toolium_examples.test_cases import SeleniumTestCase


class Actions(SeleniumTestCase):
    def test_mouse_hover(self):
        # Open url
        self.driver.get('http://the-internet.herokuapp.com/hovers')

        # Move mouse over second image
        image2 = self.driver.find_element_by_xpath("//div[@class='figure'][2]/img")
        ActionChains(self.driver).move_to_element(image2).perform()

        # Check the new element
        caption2 = self.driver.find_element_by_xpath("//div[@class='figure'][2]/div[@class='figcaption']/h5")
        assert_equal(caption2.text, 'name: user2')

    def test_keyboard_open_tab(self):
        # Open url
        self.driver.get('http://the-internet.herokuapp.com/login')

        # Open a new tab (Ctrl+t)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()

        # Close tab (Ctrl+F4)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.F4).key_up(Keys.CONTROL).perform()

        # Check that an element of the first tab is visible
        self.driver.find_element_by_id('username')
