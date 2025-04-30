import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    # Launch the browser in headless mode
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Navigate to the website
    page.goto("https://stuttgart.konsentas.de/form/7/?signup_new=1")

    # Perform actions on the page
    page.get_by_role("link", name="Ausländerbehörde - eAT-Ausgabe").click()
    page.get_by_role("button", name=" Aufenthaltstitel (eAT) - abholen").click()
    page.get_by_role("button", name="Aufenthaltstitel (eAT) - abholen", exact=True).click()
    page.get_by_role("link", name="1 Person und 2 Familienangehö").click()

    # Wait before clicking further buttons
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Weiter").click()
    page.get_by_role("button", name="Weiter").click()
    page.wait_for_timeout(2000)

    # Check for the element with the message about no available appointments
    try:
        element = page.get_by_text("Keine verfügbaren Termine!")
        page.wait_for_timeout(2000)
        
        if element.is_visible():
            element.click()
            print("Element is visible and no appointment available")
            assert page.is_visible("strong"), "Keine verfügbaren Termine!"  # Assert if 'strong' text is visible, as per the page content
        else:
            print("Element not visible or clickable")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Close the browser and context
    context.close()
    browser.close()

@pytest.mark.parametrize("playwright", [sync_playwright()], indirect=True)
def test_appoint_eAT(playwright):
    run(playwright)
