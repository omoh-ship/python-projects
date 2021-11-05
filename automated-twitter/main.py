import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


PROMISED_DOWN = 10.3
PROMISED_UP = 7.65
CHROME_DRIVER_PATH = "C:\Tools\chromedriver_win32\chromedriver.exe"
TWITTER_EMAIL = "isedugloria@gmail.com"
TWITTER_PASSWORD = "mvemjsu9p"


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        accept_tc = self.driver.find_element_by_id('_evidon-banner-acceptbutton')
        accept_tc.click()
        time.sleep(2)
        start = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start.click()
        time.sleep(60)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        # print(f'down: {down.text}')
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        # print(f'up: {up.text}')

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        username = self.driver.find_element_by_name('username')
        username.send_keys(TWITTER_EMAIL)
        username.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element_by_name('password')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(15)
        tweet_text = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div/span')
        tweet_text.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        time.sleep(2)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
        tweet_button.click()


twitter_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)

twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
