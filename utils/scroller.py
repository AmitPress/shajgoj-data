import time
def scroll_down(driver):
    SCROLL_PAUSE_TIME = 3
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # driver.execute_script("window.history.scrollRestoration = 'manual'")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        print(new_height, last_height)
        if new_height == last_height:
            break
        last_height = new_height