from playwright.sync_api import expect
from pages.landing_page import LandingPage
from pages.login_page import LoginPage


def test_login_incorrect_credentials(preCondition, env_settings):
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

    landing.navigate_to_login_page()

    login = LoginPage(page)

    email = "testinvalid@gmail.com"
    password = "Test1234"

    expect(login.login_header).to_be_visible()
    login.login_to_account(email, password)

    expect(login.login_error).to_be_visible(timeout=5000)
