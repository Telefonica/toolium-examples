# -*- coding: utf-8 -*-
u"""
Copyright 2016 Telefónica Investigación y Desarrollo, S.A.U.

The copyright to the software program(s) is property of Telefonica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefonica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
"""

from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from mobile_behave.pageobjects.shop import BaseShopPageObject
from toolium.pageelements import *
from toolium.pageobjects.mobile_page_object import MobilePageObject


class BaseInitialPageObject(MobilePageObject):
    def wait_until_loaded(self):
        """Wait until page is loaded

        :returns: initial page object
        """
        self.country.wait_until_visible(20)
        return self


class AndroidInitialPageObject(BaseInitialPageObject):
    country = Button(By.ID, 'bf.io.openshop:id/splash_shop_selection_spinner')
    english = Button(By.XPATH, '//android.widget.TextView[@text="English"]')
    accept = Button(By.ID, 'bf.io.openshop:id/splash_continue_to_shop_btn')

    def go_to_shop(self):
        """Go to shop page

        :returns: shop page object
        """
        try:
            self.accept.click()
        except NoSuchElementException:
            # Language selection is mandatory on Android 6.0
            self.country.click()
            self.english.click()
            self.accept.click()
        return BaseShopPageObject()


class IosInitialPageObject(BaseInitialPageObject):
    country = Button(By.XPATH, '//XCUIElementTypeButton[1]')
    accept = Button(By.XPATH, '//XCUIElementTypeButton[2]')
    skip = Button(By.XPATH, '//XCUIElementTypeButton[4]')
    alert = PageElement(By.XPATH, "(//XCUIElementTypeOther)[15]")  # TODO: check name=='APNSAlert'

    def go_to_shop(self):
        """Go to shop page

        :returns: shop page object
        """
        self.accept.click()
        # Skip register step
        self.skip.click()
        # Close offers alert
        self.alert.wait_until_visible()
        TouchAction(self.driver).press(x=100, y=100).release().perform()
        return BaseShopPageObject()
