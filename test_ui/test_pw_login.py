from playwright.sync_api import Playwright, sync_playwright
import pytest


def test_login(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://www.uitestingplayground.com/sampleapp')
    page.locator('//input[@placeholder="User Name"]').fill('Test')
    page.locator('//input[@name="Password"]').fill('pwd')
    page.locator('#login').click()
    #Assert
    assert page.inner_text('#loginstatus') == 'Welcome, Test'

