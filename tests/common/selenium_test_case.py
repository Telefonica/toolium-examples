import unittest
from pageobjects.common import selenium_driver

class SeleniumTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = selenium_driver.connect()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()
