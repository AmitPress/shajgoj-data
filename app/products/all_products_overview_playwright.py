from playwright.sync_api import sync_playwright
from utils.csv_saver import make_df_list
from utils.playwright_scroller import scroll_down
from bs4 import BeautifulSoup
def runner():
    categories = ['skin', 'personal-care', 'makeup', 'face', 'lips', 'eyes', 'nails', 'tools-&-brushes', 'top-brands', 'makeup-kits', 'natural', 'hair', 'mid-summer-clearance-sale-2023', 'men', 'fragrance', 'offers', 'mom-&-baby', 'buy-1-get-1', 'beauty-bonanza-clearance-sale', 'combo', 'lingerie', 'clothing-&-more', 'appliances', 'uncategorized']
    base_url = "https://shop.shajgoj.com"
    prefix = "/product-category"
    with sync_playwright() as playwright:
        tag_selector = """
        {
            // Returns the first element matching given selector in the root's subtree.
            query(root, selector) {
                return root.querySelector(selector);
            },
            // Returns all elements matching given selector in the root's subtree.
            queryAll(root, selector) {
                return Array.from(root.querySelectorAll(selector));
            }
        }"""
        playwright.selectors.register("tag", tag_selector)
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        for cat in categories:
            url = base_url+prefix+"/"+cat
            products = list()
            page.goto(url)
            scroll_down(page)
            # .alg-hit__details
            soup = BeautifulSoup(page.content(), features="lxml")
            elems = soup.find_all("div", {"class": "alg-hit__details"})
            # elems = page.locator(".alg-hit__details")
            # print(elems)
            for elem in elems:
                product_title = elem.find(attrs={"class": "product_title"}).text
                # print(product_title)
                try:
                    product_ribbon = elem.find(attrs={"class": "product_ribbon"}).text.strip()
                except:
                    product_ribbon = 'nan'
                try:
                    product_prev_price = elem.find(attrs={"class": "alg-hit__previousprice"}).text.strip()
                except:
                    product_prev_price = 'nan'
                try:
                    product_curr_price = elem.find(attrs={"class": "alg-hit__currentprice"}).text.strip()
                except:
                    product_curr_price = 'nan'
                try:
                    product_app_price = elem.find(attrs={"class": "alg-app-price"}).text.strip()
                except:
                    product_app_price = 'nan'
                try:
                    product_weight = elem.find(attrs={"class": "alg-variation"}).text.strip()
                except:
                    product_weight = 'nan'
                product = (cat, product_title, product_ribbon, product_prev_price, product_curr_price, product_app_price, product_weight)
                products.append(product)
            columns = ['category', 'product_title', 'product_ribbon', 'product_prev_price', 'product_curr_price', 'product_app_price', 'product_weight']
            make_df_list(f'{cat}_products', products, columns=columns)
