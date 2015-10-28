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
from toolium_examples.pageobjects.android.drag_and_drop import DragAndDropPageObject


class Gestures(AndroidTestCase):
    def test_drag_and_drop(self):
        # Open drag_and_drop activity
        MenuPageObject().open_option('Views').open_option('Drag and Drop')
        drag_and_drop_page = DragAndDropPageObject()

        # Drag and drop an element into another
        drag_and_drop_page.drag_and_drop()

        # Check movement
        result = self.driver.find_element_by_id('io.appium.android.apis:id/drag_result_text')
        self.assertEqual('Dropped!', drag_and_drop_page.result.text)
