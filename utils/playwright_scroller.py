import time
def scroll_down(page):
    end = page.evaluate("document.body.scrollHeight")
    while True:
        # jump to that end
        page.mouse.wheel(0, int(end))
        time.sleep(3)
        newend = page.evaluate("document.body.scrollHeight")
        print(end, newend)
        if end == newend:
            print("We are done")
            break
        else:
            end = newend