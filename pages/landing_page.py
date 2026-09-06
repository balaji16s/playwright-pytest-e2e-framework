import re
from playwright.sync_api import Page

class LandingPage:
    def __init__(self, page:Page):
        self.page = page

        # Playwright automatically handles partial matching and strips icon spaces!
        self.logo = page.get_by_role("link", name="Website for automation practice")
        self.nav_home = page.get_by_role("link", name="Home")
        self.nav_products = page.get_by_role("link", name="Products")
        self.nav_cart = page.get_by_role("link", name="Cart")
        
        # Fixed: Using re.compile without the slash to bypass Playwright's internal parser bug
        self.nav_login = page.get_by_role("link", name=re.compile("Signup", re.I))
        
        # Fixed: Avoid strict mode violation by scoping to the navbar list container first
        self.nav_test_cases = page.locator(".navbar-nav").get_by_role("link", name="Test Cases")
        
        self.nav_api_testing = page.locator(".navbar-nav").get_by_role("link", name="API Testing")
        self.nav_video_tutorials = page.get_by_role("link", name="Video Tutorials")
        self.nav_contact_us = page.get_by_role("link", name="Contact us")
