# Utils/utils.py

from playwright.sync_api import Page

def wait_and_click(page: Page, selector: str, timeout: int = 5000):
    """Wait for selector and then click."""
    page.wait_for_selector(selector, timeout=timeout)
    page.click(selector)
