from collections import defaultdict
from utils.csv_saver import make_df
from utils.get_driver import get_driver
from selenium.webdriver.common.by import By

def find_categories():
    with get_driver() as driver:
        url = "https://shop.shajgoj.com/product-category/makeup/"
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(5)
        cat_options = driver.find_element(By.CSS_SELECTOR, ".ais-hierarchical-menu--list__lvl0 , .ais-hierarchical-menu--link")
        q = cat_options.text.split("\n")
        cat_vs_amnt = defaultdict()
        while q:
            k, v = q.pop(0), q.pop(0)
            sanitized_v = "".join([c for c in v if c != ','])
            cat_vs_amnt[k] = int(sanitized_v)
        
        # make_df("categories_count", cat_vs_amnt, columns=['Category', 'Count']) # uncomment to save
        print(cat_vs_amnt.keys())