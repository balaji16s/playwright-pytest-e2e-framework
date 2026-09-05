from config.settings import settings

def test_settings_load():
    assert settings.BASE_URL is not None
    print(settings.BASE_URL)