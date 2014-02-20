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
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import logging.config
import ConfigParser


class SeleniumWrapper(object):
    # Singleton instance
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # Configure logger
            logging.config.fileConfig('logging.conf')
            cls.logger = logging.getLogger(__name__)

            # Read properties file
            cls.config = ConfigParser.ConfigParser()
            cls.config.read('properties.cfg')

            # Create new instance
            cls._instance = super(SeleniumWrapper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self):
        """
        Set up the browser driver
        """
        if self.config.get('Server', 'enabled') == 'true':
            self._setup_remotedriver()
        else:
            self._setup_localdriver()

        return self.driver

    def _setup_remotedriver(self):
        """
        Setup webdriver in a remote server
        """
        self.logger.info("Creating remote driver (browser = {0})".format(self.config.get('Browser', 'browser')))

        server_host = self.config.get('Server', 'host')
        server_port = self.config.get('Server', 'port')
        server_url = 'http://{0}:{1}/wd/hub'.format(server_host, server_port)

        capabilities_list = {
                        'firefox': DesiredCapabilities.FIREFOX,
                        'chrome': DesiredCapabilities.CHROME,
                        'iexplore': DesiredCapabilities.INTERNETEXPLORER,
                        'phantomjs': DesiredCapabilities.PHANTOMJS,
                       }
        capabilities = capabilities_list.get(self.config.get('Browser', 'browser'))
        self.driver = webdriver.Remote(command_executor=server_url, desired_capabilities=capabilities)

    def _setup_localdriver(self):
        """
        Setup webdriver in local machine
        """
        self.logger.info("Creating local driver (browser = {0})".format(self.config.get('Browser', 'browser')))

        def unknown_driver():
            assert False, 'Unknown driver {0}'.format(self.config.get('Browser', 'browser'))

        browser_config = {
                          'firefox': self._setup_firefox,
                          'chrome': self._setup_chrome,
                          'iexplore': self._setup_explorer,
                          'phantomjs': self._setup_phantomjs,
                         }

        browser_config.get(self.config.get('Browser', 'browser'), unknown_driver)()

    def _setup_firefox(self):
        """
        Setup Firefox webdriver
        """
        try:
            profile = webdriver.FirefoxProfile()
            profile.native_events_enabled = True
            self.driver = webdriver.Firefox(firefox_profile=profile)
        except:
            message = "Firefox driver can not be launched."
            self.logger.error(message)
            assert False, message

    def _setup_chrome(self):
        """
        Setup Chrome webdriver
        """
        options = webdriver.ChromeOptions()
        try:
            chromedriver = self.config.get('Browser', 'chromedriver_path')
            self.driver = webdriver.Chrome(chromedriver, chrome_options=options)
        except:
            message = "Chrome driver can not be launched. Path given in properties: %s " % (chromedriver)
            self.logger.error(message)
            assert False, message

    def _setup_explorer(self):
        """
        Setup Internet Explorer webdriver
        """
        try:
            explorerdriver = self.config.get('Browser', 'explorerdriver_path')
            self.driver = webdriver.Ie(explorerdriver)
        except:
            message = "Explorer driver can not be launched. Path given in properties: %s " % (explorerdriver)
            self.logger.error(message)
            assert False, message

    def _setup_phantomjs(self):
        """
        Setup phantomjs webdriver
        """
        try:
            phantomdriver = self.config.get('Browser', 'phantomdriver_path')
            self.driver = webdriver.PhantomJS(executable_path=phantomdriver)
        except:
            message = "Phantom driver can not be launched. Path given in properties: %s " % (phantomdriver)
            self.logger.error(message)
            assert False, message
