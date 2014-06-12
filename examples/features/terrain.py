from lettuce import before, after, world
from selenium_tid_python import selenium_driver


@before.all
def setup_browser():
    world.driver = selenium_driver.connect()


@after.all
def teardown_browser(total):
    world.driver.quit()
