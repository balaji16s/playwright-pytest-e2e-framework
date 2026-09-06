import pytest
from playwright.sync_api import Page
from config.settings import settings

@pytest.fixture
def env_settings():
    return settings

@pytest.fixture
def preCondition(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    app_page = context.new_page()
    yield app_page
    app_page.close()
    context.close()
    browser.close()
