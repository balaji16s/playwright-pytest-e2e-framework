from playwright.sync_api import Page

class DeleteAccount():
    def __init__(self, page:Page):
        self.page = page

        self.delete_account_header = page.get_by_text("Account Deleted!")
        self.delete_account_message = page.get_by_text("Your account has been permanently deleted!")
        self.delete_account_continue_button = page.get_by_role("link", name="Continue")
