from playwright.sync_api import sync_playwright


def test_successful_login_logout():
    user = {'username': 'tomsmith', 'password': 'SuperSecretPassword!'}
    expected_login_message = "You logged into a secure area!"
    expected_logout_message = "You logged out of the secure area!"

    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()

        # Open url
        page.goto('http://the-internet.herokuapp.com/login')

        # Login and check welcome message
        page.get_by_label('Username').fill(user['username'])
        page.get_by_label('Password').fill(user['password'])
        page.locator("xpath=//form[@id='login']/button").click()
        message = page.locator('id=flash').inner_text().splitlines()[0]
        assert expected_login_message in message

        # Logout and check logout message
        page.locator("xpath=//div[@id='content']//a[contains(@class,'button')]").click()
        message = page.locator('id=flash').inner_text().splitlines()[0]
        assert expected_logout_message in message

        browser.close()
