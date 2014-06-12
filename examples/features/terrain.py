from lettuce import before, after, world
from selenium_tid_python import selenium_driver
from selenium_tid_python.utils import Utils
import logging
import sys


@before.each_scenario
def setup_driver(scenario):
    # Configure logger
    world.logger = logging.getLogger()
    # Create driver
    if not hasattr(world, 'driver') or world.driver == None:
        world.driver = selenium_driver.connect()
    # Add implicitly wait
    config = selenium_driver.config
    implicitly_wait = config.get_optional('Common', 'implicitly_wait')
    if (implicitly_wait):
        world.driver.implicitly_wait(implicitly_wait)
    # Maximize browser
    if selenium_driver.is_maximizable():
        world.driver.maximize_window()


@after.each_scenario
def teardown_driver(scenario):
    # Check test result
    result = sys.exc_info()
    if result != (None, None, None):
        # TODO: the error check is wrong, never enters here
        Utils(world.driver).capture_screenshot(scenario.name.replace(' ', '_'))

    # Close browser and stop driver
    config = selenium_driver.config
    reuse_driver = config.get_optional('Common', 'reuse_driver')
    if not reuse_driver:
        world.driver.quit()
        world.driver = None


@after.all
def teardown_driver_all(total):
    if hasattr(world, 'driver') and world.driver != None:
        world.driver.quit()
        world.driver = None
