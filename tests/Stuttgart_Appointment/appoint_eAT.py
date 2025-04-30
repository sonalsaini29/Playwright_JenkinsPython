import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://stuttgart.konsentas.de/form/7/?signup_new=1")
    page.get_by_role("link", name="Ausländerbehörde - eAT-Ausgabe").click()
    page.get_by_role("button", name=" Aufenthaltstitel (eAT) - abholen").click()
    page.get_by_role("button", name="Aufenthaltstitel (eAT) - abholen", exact=True).click()
    page.get_by_role("link", name="1 Person und 2 Familienangehö").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Weiter").click()
    page.get_by_role("button", name="Weiter").click()
    page.wait_for_timeout(2000)
    element = page.get_by_text("Keine verfügbaren Termine!")
    page.wait_for_timeout(2000)
    if element.is_visible():
        element.click()
        print("Element is visible and no appointment available")
    else:
        print("Element not visible or clickable")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)