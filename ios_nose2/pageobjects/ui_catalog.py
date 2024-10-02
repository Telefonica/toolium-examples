# -*- coding: utf-8 -*-
u"""
Copyright 2024 Telefónica Investigación y Desarrollo, S.A.U.
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

from appium.webdriver.common.appiumby import AppiumBy

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class UICatalogHome(PageObject):
    page_title  = Text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "UIKitCatalog"`]', 
                       wait=True)
    alerts_view = Button(AppiumBy.IOS_PREDICATE, 'label == "Alert Views"')
    webview_view = Button(AppiumBy.IOS_PREDICATE, 'label == "Web View"')

class UIAlertsView(PageObject):
    page_title = Text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Alert Views"`]', 
                      wait=True)
    simple = Button(AppiumBy.IOS_PREDICATE, 'label == "Simple"')
    alert = PageElement(AppiumBy.CLASS_NAME, 'XCUIElementTypeAlert')

class UIWebViewView(PageObject):
    page_title = Text(AppiumBy.IOS_CLASS_CHAIN, '**/XCUIElementTypeStaticText[`label == "Web View"`]',
                      wait=True)

