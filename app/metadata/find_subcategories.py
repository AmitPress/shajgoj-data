# no need to use selenium
from utils.csv_saver import make_df_list
from utils.get_driver import get_driver
from selenium.webdriver.common.by import By
# from parsel import Selector
# import requests

categories = ['Skin', 'Personal care', 'Makeup', 'Face', 'Lips', 'Eyes', 'Nails', 'Tools & Brushes', 'Top Brands', 'Makeup Kits', 'Natural', 'Hair', 'Men', 'Fragrance', 'lingerie', 'Clothing & More']
categories_url = ['-'.join(cat.lower().split(' ')) for cat in categories]
# print(categories)
# def find_subcategories():
#     result = list()
#     for cat in categories:
#         url = f"https://shop.shajgoj.com/product-category/{cat}"
#         try:
#             rqst = requests.get(url)
#             if rqst.status_code == 404:
#                 print("404", cat)
#             source = rqst.text
#         except:
#             print("Error Fetching")
#         page = Selector(source)
#         items = page.css(".ais-hierarchical-menu--link")
#         print(items)

def find_subcategories():
    result = list()

    with get_driver() as driver:
        for cat, catu in zip(categories, categories_url):
            url = f"https://shop.shajgoj.com/product-category/{catu}"
            driver.get(url)
            driver.implicitly_wait(5)
            elems = driver.find_elements(By.CSS_SELECTOR, '.ais-hierarchical-menu--list__lvl1')
            for elem in elems:
                q = elem.text.split('\n')
                while q:
                    f, s= q.pop(0), q.pop(0)
                    s = int("".join([c for c in s if c != ',']))
                    result.append((f, s, cat))
    
    print(result)
