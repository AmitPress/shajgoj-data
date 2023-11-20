## Edge driver
from contextlib import contextmanager
from selenium.webdriver import Edge, EdgeOptions, EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
try:
    edge_driver_manager = EdgeChromiumDriverManager().install()
except:
    raise Exception("Error Downloading Driver Manager")

@contextmanager
def get_driver():
    # settings
    options = EdgeOptions()
    # prefs = {"profile.managed_default_content_settings.images": 2}
    # options.add_experimental_option("prefs", prefs)
    service = EdgeService(
        edge_driver_manager
    )
    session = Edge(service=service, options=options)
    try:
        yield session
    except Exception as e:
        print(str(e))
        session.close()
    finally:
        session.quit()