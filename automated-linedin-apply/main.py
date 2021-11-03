import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


chrome_driver_path = "C:\Tools\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2&f_WT=2&keywords=python%20developer")
driver.maximize_window()

# time.sleep(6)
sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()

sign_in_text_field = driver.find_element_by_name("session_key")
sign_in_text_field.send_keys("your_email@email.com")
sign_in_text_field.send_keys(Keys.ARROW_DOWN)
password = driver.find_element_by_name("session_password")
password.send_keys("password")

password.send_keys(Keys.ENTER)

jobs = driver.find_elements_by_css_selector(".jobs-search-results__list-item")
# new = [job.click for job in jobs]
# jobs.click()
for job in jobs:
    # print(job.text)
    job.click()
    # time.sleep()
    save = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div/div/div[1]/div/'
                                    'div[1]/div/div[2]/div[3]/div/button')

driver.quit()

