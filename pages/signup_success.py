from playwright.sync_api import Page

class SignupSuccess():
    def __init__(self, page:Page):
        self.page = page

        self.confirm_header = page.get_by_text("Account Created!")
        self.confirm_message = page.get_by_text("Congratulations! Your new account has been successfully created!")
        self.continue_button = page.get_by_role("link", name="Continue")
