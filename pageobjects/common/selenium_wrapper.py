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
        print config.get('Selenium', 'browser')
        self.driver = webdriver.Firefox()
        return self.driver
    