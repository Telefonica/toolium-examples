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
            logging.config.fileConfig('conf/logging.conf')
            cls.logger = logging.getLogger(__name__)

            # Read properties file
            cls.config = ConfigParser.ConfigParser()
            cls.config.read('conf/properties.cfg')

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
        browser = self.config.get('Browser', 'browser')
        self.logger.info("Creating remote driver (browser = {0})".format(browser))

        server_host = self.config.get('Server', 'host')
        server_port = self.config.get('Server', 'port')
        server_url = 'http://{0}:{1}/wd/hub'.format(server_host, server_port)

        # Get browser type capabilities
        capabilities_list = {
                             'firefox': DesiredCapabilities.FIREFOX,
                             'chrome': DesiredCapabilities.CHROME,
                             'safari': DesiredCapabilities.SAFARI,
                             'opera': DesiredCapabilities.OPERA,
                             'iexplore': DesiredCapabilities.INTERNETEXPLORER,
                             'phantomjs': DesiredCapabilities.PHANTOMJS,
                             'android': DesiredCapabilities.ANDROID,
                             'iphone': DesiredCapabilities.IPHONE,
                            }
        browser_name = browser.split('-')[0]
        capabilities = capabilities_list.get(browser_name)

        # Add browser version
        try:
            capabilities['version'] = browser.split('-')[1]
        except:
            pass

        # Add platform capability
        try:
            platforms_list = {
                              'xp': 'XP',
                              'windows_7': 'VISTA',
                              'windows_8': 'WIN8',
                              'linux': 'LINUX',
                              'mac': 'MAC',
                             }
            capabilities['platform'] = platforms_list.get(browser.split('-')[3])
        except:
            pass

        # Create remote driver
        self.driver = webdriver.Remote(command_executor=server_url, desired_capabilities=capabilities)

    def _setup_localdriver(self):
        """
        Setup webdriver in local machine
        """
        browser = self.config.get('Browser', 'browser')
        browser_name = browser.split('-')[0]
        self.logger.info("Creating local driver (browser = {0})".format(browser))

        def unknown_driver():
            assert False, 'Unknown driver {0}'.format(browser_name)

        browser_config = {
                          'firefox': self._setup_firefox,
                          'chrome': self._setup_chrome,
                          'safari': self._setup_safari,
                          'opera': self._setup_opera,
                          'iexplore': self._setup_explorer,
                          'phantomjs': self._setup_phantomjs,
                          'android': self._setup_android,
                          'iphone': self._setup_iphone,
                         }

        try:
            browser_config.get(browser_name, unknown_driver)()
        except Exception as e:
            message = "{0} driver can not be launched: {1}".format(browser_name.title(), e)
            self.logger.error(message)
            assert False, message

    def _setup_firefox(self):
        """
        Setup Firefox webdriver
        """
        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = True
        self.driver = webdriver.Firefox(firefox_profile=profile)

    def _setup_chrome(self):
        """
        Setup Chrome webdriver
        """
        chromedriver = self.config.get('Browser', 'chromedriver_path')
        self.logger.debug("Chrome driver path given in properties: {0}".format(chromedriver))
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(chromedriver, chrome_options=options)

    def _setup_safari(self):
        """
        Setup Safari webdriver
        """
        self.driver = webdriver.Safari()

    def _setup_opera(self):
        """
        Setup Opera webdriver
        """
        seleniumserver = self.config.get('Browser', 'seleniumserver_path')
        self.logger.debug("Selenium server path given in properties: {0}".format(seleniumserver))
        self.driver = webdriver.Opera(seleniumserver)

    def _setup_explorer(self):
        """
        Setup Internet Explorer webdriver
        """
        explorerdriver = self.config.get('Browser', 'explorerdriver_path')
        self.logger.debug("Explorer driver path given in properties: {0}".format(explorerdriver))
        self.driver = webdriver.Ie(explorerdriver)

    def _setup_phantomjs(self):
        """
        Setup phantomjs webdriver
        """
        phantomdriver = self.config.get('Browser', 'phantomdriver_path')
        self.logger.debug("Phantom driver path given in properties: {0}".format(phantomdriver))
        self.driver = webdriver.PhantomJS(executable_path=phantomdriver)

    def _setup_android(self):
        """
        Setup Android webdriver
        """
        assert False

    def _setup_iphone(self):
        """
        Setup Iphone webdriver
        """
        assert False
