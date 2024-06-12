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

from selenium.webdriver.common.by import By

from ios_nose2.pageobjects.ui_catalog import UICatalogHome, UIWebViewView
from ios_nose2.test_cases import IosTestCase


class IosHybrid(IosTestCase):
    def test_webview(self):
         # Open app
        home_page = UICatalogHome()
        home_page.webview_view.click()
        web_view_page = UIWebViewView()

        # Switch to webview context
        self.utils.switch_to_first_webview_context()
        self.logger.debug(f"Context: {self.driver_wrapper.driver.contexts}")    

        # Get title in webview
        title_text = self.utils.wait_until_element_visible((By.XPATH, '//h1'))
        print(title_text.text)

        # Assert title text
        assert "This is HTML" in title_text.text, 'Title text is not correct'
