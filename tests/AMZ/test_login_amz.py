from playwright.sync_api import sync_playwright, expect
from Utils.utils import common_utils
from Utils.webelements import AmazonHomePage

def test_login_amz():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Launch in non-headless mode
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.amazon.in/")
        common_utils.wait_and_click(page, AmazonHomePage.SIGN_IN_LINK)
        # page.get_by_role("link", name="Hello, sign in Account & Lists").click()
        # page.get_by_role("textbox", name="Enter your mobile number or").click()
        # page.get_by_role("textbox", name="Enter your mobile number or").fill("semail ID)
        # page.get_by_role("button", name="Continue").click()
        # page.get_by_role("textbox", name="Password").fill("Password)
        # page.get_by_role("button", name="Sign in").click()
        # page.wait_for_timeout(1000)
        # page.get_by_role("button", name="Open All Categories Menu").hover()
        # page.wait_for_timeout(1000)
        # page.get_by_role("button", name="Open All Categories Menu").click()
        # page.get_by_role("heading", name="Shop by Category").scroll_into_view_if_needed()
        # page.wait_for_timeout(1000)
        # page.get_by_role("link", name="See All Categories").click()
        # page.wait_for_timeout(1000)
        # page.get_by_role("button", name="Toys, Baby Products, Kids'").click()
        # page.wait_for_timeout(1000)
        # page.get_by_role("link", name="Baby Products").click()
        # page.wait_for_timeout(1000)
        # page.get_by_role("link", name="Diapers & Wipes").click()
        # # expect(page.locator("#a-page")).to_match_aria_snapshot("- heading \"Best deals on diapers\" [level=2]")
        # page.get_by_role("link", name="1 to 5kg").click()
        
        # context.close()
        # browser.close()

# Running the test
if __name__ == "__main__":
    test_login_amz()