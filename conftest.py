import pytest
from playwright.sync_api import Page
from config.settings import settings
from playwright.sync_api import expect

@pytest.fixture
def env_settings():
    return settings

@pytest.fixture
def preCondition(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    app_page = context.new_page()

    app_page.set_default_timeout(settings.DEFAULT_TIMEOUT)
    app_page.set_default_navigation_timeout(settings.DEFAULT_TIMEOUT)
    expect.set_options(timeout=settings.DEFAULT_TIMEOUT)

    yield app_page

    app_page.close()
    context.close()
    browser.close()
