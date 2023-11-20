
from utils.csv_saver import make_df_list
from utils.get_driver import get_driver
from selenium.webdriver.common.by import By

def find_subsubcategories_cavernous():
    with get_driver() as driver:
        result = list()
        url = f"https://shop.shajgoj.com/product-category/makeup/#q=&hPP=21&idx=wp_posts_product&p=0&hFR%5Btaxonomies_hierarchical.product_cat.lvl0%5D%5B0%5D=Personal%20care%20%3E%20Wellness%20%3E%20Shop%20By%20Concern&is_v=1"
        driver.get(url)
        driver.implicitly_wait(4)
        try:
            elems = driver.find_elements(By.CSS_SELECTOR, '.ais-hierarchical-menu--list__lvl2')
        except:
            print("Exception Occured")
        for elem in elems:
            q = elem.text.split('\n')
            while q:
                f, s= q.pop(0), q.pop(0)
                s = int("".join([c for c in s if c != ',']))
                result.append((f, s, "Wellness/Shop By Concern"))
    make_df_list('find_subsubcategories_cavernous', result, ['SubSubCategory', 'Count', 'Parent'])
    print(result)