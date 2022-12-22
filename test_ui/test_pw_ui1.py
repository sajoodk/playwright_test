from playwright.sync_api import Playwright, expect
from home_page_elements import Homepage

def test_run(playwright: Playwright) -> None:
    #Assess/Given
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    #Act/When
    page.goto('https://ecommerce-playground.lambdatest.io/')
    page.locator("text=Shop by Category").click()
    page.set_default_timeout(10000)

    #Assert/Then
    home_page = Homepage(page)
    expect(home_page.camera_locator).to_have_text("Cameras")