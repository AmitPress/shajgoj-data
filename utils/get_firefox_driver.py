## Firefox driver
from contextlib import contextmanager
from selenium.webdriver import Firefox, FirefoxOptions, FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
try:
    firefox_driver_manager = GeckoDriverManager().install()
except:
    raise Exception("Error Downloading Driver Manager")

@contextmanager
def get_driver():
    # settings
    options = FirefoxOptions()
    # prefs = {"profile.managed_default_content_settings.images": 2}
    # options.add_experimental_option("prefs", prefs)
    service = FirefoxService(
        firefox_driver_manager
    )
    session = Firefox(service=service, options=options)
    try:
        yield session
    except Exception as e:
        print(str(e))
        session.close()
    finally:
        session.quit()