from selenium import selenium
from selenium import webdriver

class SeleniumWrapper(object):
    # singleton
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SeleniumWrapper, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def connect(self):
        self.driver = webdriver.Firefox()
        return self.driver
    