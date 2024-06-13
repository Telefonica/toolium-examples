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

from ios_nose2.pageobjects.ui_catalog import UICatalogHome, UIAlertsView
from ios_nose2.test_cases import IosTestCase


class IosTestApp(IosTestCase):
    def test_alert_is_shown(self):
        # Open app
        home_page = UICatalogHome()
        home_page.alerts_view.click()

        # Click on Simple alert
        alert_page = UIAlertsView()
        alert_page.simple.click()

        # Check that the alert is shown
        assert alert_page.alert.is_visible(), 'Alert is not shown'

