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
from selenium import webdriver
import ConfigParser
import os

config = ConfigParser.ConfigParser()
config.read('properties.cfg')


class SeleniumWrapper(object):
    # singleton
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SeleniumWrapper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self):
        """
        Set up the browser driver
        """
        def unknown_driver():
            assert False, 'Unknown driver {0}'.format(config.get('Browser', 'browser'))

        browser_config = {'firefox': self._setup_firefox,
                          'chrome': self._setup_chrome,
                          'iexplore': self._setup_explorer,
                          'phantomjs': self._setup_phantomjs}

        browser_config.get(config.get('Browser', 'browser'), unknown_driver)()
        return self.driver

    def _setup_firefox(self):
        """
        Setup Firefox webdriver
        """
        try:
            profile = webdriver.FirefoxProfile()
            profile.native_events_enabled = True
            self.driver = webdriver.Firefox(firefox_profile=profile)
        except:
            assert False, "Firefox driver can not be launched."

    def _setup_chrome(self):
        """
        Setup Chrome webdriver
        """
        options = webdriver.ChromeOptions()
        try:
            chromedriver = config.get('Browser', 'chromedriver_path')
            self.driver = webdriver.Chrome(chromedriver, chrome_options=options)
        except:
            assert False, "Chrome driver can not be launched. Path given in properties: %s " % (chromedriver)

    def _setup_explorer(self):
        """
        Setup Internet Explorer webdriver
        """
        try:
            explorerdriver = config.get('Browser', 'explorerdriver_path')
            self.driver = webdriver.Ie(explorerdriver)
        except:
            assert False, "Explorer driver can not be launched. Path given in properties: %s " % (explorerdriver)

    def _setup_phantomjs(self):
        """
        Setup phantomjs webdriver
        """
        try:
            phantomdriver = config.get('Browser', 'phantomdriver_path')
            self.driver = webdriver.PhantomJS(executable_path=phantomdriver)
        except:
            assert False, "Phantom driver can not be launched. Path given in properties: %s " % (phantomdriver)
