from utils.get_chrome_driver import get_driver
from selenium.webdriver.common.by import By
from utils.csv_saver import make_df_list
from utils.scroller import scroll_down
categories = ['skin', 'personal-care', 'makeup', 'face', 'lips', 'eyes', 'nails', 'tools-&-brushes', 'top-brands', 'makeup-kits', 'natural', 'hair', 'mid-summer-clearance-sale-2023', 'men', 'fragrance', 'offers', 'mom-&-baby', 'buy-1-get-1', 'beauty-bonanza-clearance-sale', 'combo', 'lingerie', 'clothing-&-more', 'appliances', 'uncategorized']
base_url = "https://shop.shajgoj.com"
prefix = "/product-category"

# basically scrapes all the product cards as of now
def scrape_all_product_card():
    for cat in categories:
        url = base_url+prefix+"/"+cat
        products = list()
        with get_driver() as driver:
            driver.get(url)
            driver.maximize_window()
            scroll_down(driver=driver)
            elems = driver.find_elements(By.CLASS_NAME, "alg-hit__details")
            for elem in elems:
                product_title = elem.find_element(By.CLASS_NAME, "product_title").text
                try:
                    product_ribbon = elem.find_element(By.CLASS_NAME, "product_ribbon").text
                except:
                    product_ribbon = 'nan'
                try:
                    product_prev_price = elem.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "alg-hit__previousprice", " " ))]').text
                except:
                    product_prev_price = 'nan'
                try:
                    product_curr_price = elem.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "alg-hit__currentprice", " " ))]').text
                except:
                    product_curr_price = 'nan'
                try:
                    product_app_price = elem.find_element(By.CLASS_NAME, "alg-app-price").text
                except:
                    product_app_price = 'nan'
                try:
                    product_weight = elem.find_element(By.CLASS_NAME, "alg-variation").text
                except:
                    product_weight = 'nan'

                product = (cat, product_title, product_ribbon, product_prev_price, product_curr_price, product_app_price, product_weight)
                products.append(product)
        columns = ['category', 'product_title', 'product_ribbon', 'product_prev_price', 'product_curr_price', 'product_app_price', 'product_weight']
        make_df_list(f'{cat}_products', products, columns=columns)
        break