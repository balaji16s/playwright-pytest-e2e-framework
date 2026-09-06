from playwright.sync_api import expect
from pages.landing_page import LandingPage

def test_register_user(preCondition, env_settings):
    page = preCondition
    landing = LandingPage(page)
    page.goto(env_settings.BASE_URL)

    expect(landing.logo).to_be_visible(timeout=15_000)
    expect(landing.nav_products).to_be_visible()
    expect(landing.nav_cart).to_be_visible()
    expect(landing.nav_login).to_be_visible()
    expect(landing.nav_test_cases).to_be_visible()
    expect(landing.nav_api_testing).to_be_visible()
    expect(landing.nav_video_tutorials).to_be_visible()
    expect(landing.nav_contact_us).to_be_visible()
