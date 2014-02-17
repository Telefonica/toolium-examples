import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class RegisterUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_successfull_register(self):
        username = "user1"
        password = "pass1"
        name = "name1"
        email = "user1@mailinator.com"
        place = "Barcelona"
        expectedMessage = "The user has been registered"

        driver = self.driver
        driver.get("http://qacore01.hi.inet/sites/seleniumExamples/register.html")
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_id("name").send_keys(name)
        driver.find_element_by_id("email").send_keys(email)
        Select(driver.find_element_by_id("place")).select_by_visible_text(place)

        driver.find_element_by_id("registerButton").click()

        result_message = driver.find_element_by_xpath("//div[@id='content']/div/div/div/b[2]").text
        self.assertIn(expectedMessage, result_message)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
