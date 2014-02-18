from tests.common.selenium_test_case import SeleniumTestCase
from pageobjects.register import RegisterPageObject
from pageobjects.register_result import RegisterResultPageObject

class RegisterUser(SeleniumTestCase):
    def test_successfull_register(self):
        registerPage = RegisterPageObject()
        registerPage.username = "user1"
        registerPage.password = "pass1"
        registerPage.name = "name1"
        registerPage.email = "user1@mailinator.com"
        registerPage.place = "Barcelona"
        registerPage.submit()

        expectedMessage = "The user has been registered"
        resultPage = RegisterResultPageObject()
        self.assertIn(expectedMessage, resultPage.message)

if __name__ == "__main__":
    unittest.main()
