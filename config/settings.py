import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BASE_URL = os.getenv("BASE_URL", "https://example.com")
    API_BASE_URL = os.getenv("API_BASE_URL", "https://api.example.com")
    TEST_USERNAME = os.getenv("TEST_USERNAME")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD")
    DEFAULT_TIMEOUT = 30000  # milliseconds

settings = Settings()