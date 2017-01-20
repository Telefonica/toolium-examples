# -*- coding: utf-8 -*-
u"""
Copyright 2016 Telefónica Investigación y Desarrollo, S.A.U.

The copyright to the software program(s) is property of Telefonica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefonica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
"""

from selenium.webdriver.common.by import By

from toolium.pageelements import *
from toolium.pageobjects.mobile_page_object import MobilePageObject


class BaseShopPageObject(MobilePageObject):
    def get_collections(self):
        """Returns visible collections

        :returns: list with visible collections
        """
        return self.collections.web_elements


class AndroidShopPageObject(BaseShopPageObject):
    title = Text(By.XPATH, '//android.widget.TextView[1]')
    collections = Buttons(By.ID, 'bf.io.openshop:id/banner_image')


class IosShopPageObject(BaseShopPageObject):
    title = Text(By.XPATH, "//XCUIElementTypeStaticText[1]")
    collections = Buttons(By.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell')
