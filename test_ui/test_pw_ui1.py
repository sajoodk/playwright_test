from playwright.sync_api import Playwright, sync_playwright,expect
import pytest


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
    expect(page.locator("#widget-navbar-217841 > ul > li:nth-child(2) > a > div.info > span")).to_have_text("Cameras")