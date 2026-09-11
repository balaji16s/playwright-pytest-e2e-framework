from playwright.sync_api import expect
from pages.landing_page import LandingPage
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
from pages.signup_success import SignupSuccess
from pages.delete_account import DeleteAccount

def test_login_logout_user(preCondition, env_settings):
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

    name = "Test Valid"
    email = "testvalid@gmail.com"
    password = "Test1234"

    expect(login.signup_header).to_be_visible()
    login.signup_to_account(name, email)
    
    signup = SignupPage(page)

    expect(signup.account_info_heading).to_be_visible(timeout=15000)
    expect(signup.address_info_heading).to_be_visible()
    
    signup.title_mr.check()

    expect(signup.signup_name).to_have_value(name)
    expect(signup.signup_email).to_have_value(email)
    signup.signup_password.fill("Test1234")
    signup.signup_day.select_option("1")
    signup.signup_month.select_option("January")
    signup.signup_year.select_option("1996")

    signup.signup_newsletter.check()
    signup.signup_special_offers.check()

    signup.signup_firstname.fill("Test")
    signup.signup_lastname.fill("Valid")
    signup.signup_company.fill("Test Company")
    signup.signup_address.fill("1 test apartment test street")
    signup.signup_address2.fill("test area")
    signup.signup_country.select_option("India")
    signup.signup_state.fill("Tamil Nadu")
    signup.signup_city.fill("Test City")
    signup.signup_zipcode.fill("123456")
    signup.signup_mobile_number.fill("9876543210")

    signup.create_account.click()

    signupsuccess = SignupSuccess(page)

    expect(signupsuccess.confirm_header).to_be_visible(timeout=15000)
    expect(signupsuccess.confirm_message).to_be_visible()
    signupsuccess.continue_button.click()

    expect(landing.nav_delete_account).to_be_visible(timeout=15000)
    expect(landing.nav_Logged_in_as_username).to_be_visible()

    landing.nav_logout.click()


    expect(login.login_header).to_be_visible()
    login.login_to_account(email, password)


    expect(landing.nav_delete_account).to_be_visible(timeout=15000)
    expect(landing.nav_Logged_in_as_username).to_be_visible()


    landing.nav_logout.click()

    expect(login.login_header).to_be_visible()
    login.login_to_account(email, password)


    expect(landing.nav_delete_account).to_be_visible(timeout=15000)
    expect(landing.nav_Logged_in_as_username).to_be_visible()

    landing.nav_delete_account.click()

    deleteaccount = DeleteAccount(page)
    
    expect(deleteaccount.delete_account_header).to_be_visible(timeout=15000)
    expect(deleteaccount.delete_account_message).to_be_visible()
    deleteaccount.delete_account_continue_button.click()

    expect(landing.nav_logout).not_to_be_visible()
    expect(landing.nav_login).to_be_visible(timeout=10_000)
