from playwright.sync_api import Page

class SignupPage:
    def __init__(self, page:Page):
        self.page=page

        self.account_info_heading = page.get_by_text("Enter Account Information",exact=True)
        self.title_mr = page.get_by_label("Mr.")
        self.title_mrs = page.get_by_label("Mrs.")

        self.signup_name = page.locator('[data-qa="name"]')
        self.signup_email = page.get_by_label("Email")
        self.signup_password = page.get_by_label("Password")
        
        self.signup_day = page.locator('[data-qa="days"]')
        self.signup_month = page.locator('[data-qa="months"]')
        self.signup_year = page.locator('[data-qa="years"]')

        self.signup_newsletter = page.get_by_label("Sign up for our newsletter!")
        self.signup_special_offers = page.get_by_label("Receive special offers from our partners!")

        self.address_info_heading = page.get_by_text("Address Information",exact=True)
        self.signup_firstname = page.get_by_label("First Name")
        self.signup_lastname = page.get_by_label("Last Name")
        self.signup_company = page.locator('[data-qa="company"]')
        self.signup_address = page.locator('[data-qa="address"]')
        self.signup_address2 = page.get_by_label("Address 2")

        self.signup_country = page.get_by_label("Country")

        self.signup_state = page.get_by_label("State")
        self.signup_city = page.locator('[data-qa="city"]')
        self.signup_zipcode = page.locator('[data-qa="zipcode"]')
        self.signup_mobile_number = page.get_by_label("Mobile Number")

        self.create_account = page.get_by_role("button", name="Create Account")
