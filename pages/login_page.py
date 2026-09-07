from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page:Page):
        self.page = page

        self.login_header = page.get_by_text("Login to your account")
        self.login_email = page.locator('[data-qa="login-email"]')
        self.login_password = page.locator('[data-qa="login-password"]')
        self.login_button = page.locator('[data-qa="login-button"]')

        self.login_error = page.get_by_text("Your email or password is incorrect!")
        # self.login_success = page.get_by_text("")


        self.signup_header = page.get_by_text("New User Signup!")
        self.signup_name = page.locator('[data-qa="signup-name"]')
        self.signup_email = page.locator('[data-qa="signup-email"]')
        self.signup_button = page.locator('[data-qa="signup-button"]')
        
        self.signup_error = page.get_by_text("Email Address already exist!")
        

    def login_to_account(self,email,password):
        self.login_email.fill(email)
        self.login_password.fill(password)
        self.login_button.click()

    def signup_to_account(self,name,email):
        self.signup_name.fill(name)
        self.signup_email.fill(email)
        self.signup_button.click()