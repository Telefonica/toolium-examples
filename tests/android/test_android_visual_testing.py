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

from toolium_examples.test_cases import AndroidTestCase
from toolium_examples.pageobjects.android.menu import MenuPageObject
from toolium_examples.pageobjects.android.tabs import TabsPageObject


class Tabs(AndroidTestCase):
    def test_change_tab(self):
        # Open tabs activity
        MenuPageObject().open_option('Views').open_option('Tabs').open_option('1. Content By Id')
        tabs_page = TabsPageObject()

        # Check that the first tab is open
        self.assertEqual('tab1', tabs_page.content1.text)
        tabs_page.container.assertScreenshot('tab1')

        # Open second tab and check content
        tabs_page.tab2.click()
        self.assertEqual('tab2', tabs_page.content2.text)
        tabs_page.container.assertScreenshot('tab2')
