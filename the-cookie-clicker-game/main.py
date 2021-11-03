import time

from selenium import webdriver

chrome_driver_path = "C:\Tools\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_css_selector('#cookie')
store_items = driver.find_elements_by_css_selector("#store div")
store_items_id = [item.get_attribute("id") for item in store_items]

time_out = time.time() + 5
five_minutes = time.time() + 60 * 5
clicks = 0
while True:

    clicks += 1
    cookie.click()
    cookie_money = int(driver.find_element_by_css_selector('#money').text)

    if time.time() > time_out:
        prices = driver.find_elements_by_css_selector("#store b")
        prices_list = [int(price.text.split("-")[1].strip().replace(",", "")) for price in prices if price.text != ""]
        all_upgrades = {}
        for i in range(len(prices_list)):
            all_upgrades[prices_list[i]] = store_items_id[i]
        available_classes = {int(driver.find_element_by_id(item_id).text.split('-')[1].split('\n')[0].strip()): item_id
                             for item_id in store_items_id if driver.find_element_by_id(item_id).get_attribute('class')
                             != "grayed"}
        affordable = [price for (price, item_id) in available_classes.items()]
        try:
            highest = max(affordable)
        except ValueError:
            continue
        else:
            driver.find_element_by_id(available_classes[highest]).click()
        time_out = time.time() + 5
    if time.time() > five_minutes:
        break
        # print(prices_list)

