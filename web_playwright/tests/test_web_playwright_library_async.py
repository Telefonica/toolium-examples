import asyncio

from playwright.async_api import Playwright, async_playwright


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=True)
    context = await browser.new_context()
    page = await context.new_page()

    user = {'username': 'tomsmith', 'password': 'SuperSecretPassword!'}
    expected_login_message = "You logged into a secure area!"
    expected_logout_message = "You logged out of the secure area!"

    # Open url
    await page.goto('http://the-internet.herokuapp.com/login')

    # Login and check welcome message
    await page.get_by_label('Username').fill(user['username'])
    await page.get_by_label('Password').fill(user['password'])
    await page.locator("xpath=//form[@id='login']/button").click()
    message = await page.locator('id=flash').inner_text()
    message = message.splitlines()[0]
    assert expected_login_message in message

    # Logout and check logout message
    await page.locator("xpath=//div[@id='content']//a[contains(@class,'button')]").click()
    message = await page.locator('id=flash').inner_text()
    message = message.splitlines()[0]
    assert expected_logout_message in message

    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


# Uncomment this line to run the script, commented to avoid running it unexpectedly
asyncio.run(main())
