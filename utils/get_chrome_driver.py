from contextlib import contextmanager
from selenium.webdriver import Chrome, ChromeOptions, ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
try:
    driver_manager = ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install()
except:
    raise Exception("Error Downloading Driver Manager")

@contextmanager
def get_driver():
    # settings
    options = ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    service = ChromeService(
        driver_manager
    )
    try:
        session = Chrome(service=service, options=options)
        yield session
    except Exception as e:
        print(str(e))
        session.close()
    finally:
        session.quit()

