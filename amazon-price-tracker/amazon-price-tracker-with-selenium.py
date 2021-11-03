from selenium import webdriver

chrome_driver_path = "C:\Tools\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.amazon.com/HP-Touchscreen-i5-1135G7-Streaming-14-dw1024nr/dp/"
           "B091D6F3JP/ref=sr_1_4?dchild=1&keywords=hp+ssd+laptop+with+pen&qid=1632748735&sr=8-4")

price = driver.find_element_by_id("priceblock_ourprice")
print(price.text)

driver.quit()
