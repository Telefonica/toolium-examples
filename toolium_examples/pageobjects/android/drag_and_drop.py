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
from appium.webdriver.common.touch_action import TouchAction

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class DragAndDropPageObject(PageObject):
    dot1 = PageElement(By.ID, 'io.appium.android.apis:id/drag_dot_1')
    dot2 = PageElement(By.ID, 'io.appium.android.apis:id/drag_dot_2')
    dot3 = PageElement(By.ID, 'io.appium.android.apis:id/drag_dot_3')
    result = Text(By.ID, 'io.appium.android.apis:id/drag_result_text')

    def drag_and_drop(self):
        TouchAction(self.driver).long_press(self.dot3.element()).move_to(self.dot2.element()).release().perform()
