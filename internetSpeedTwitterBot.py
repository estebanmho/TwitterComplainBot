import os

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

PASSWORD = os.environ.get("PASSWORD")
EMAIL = os.environ.get("EMAIL")


class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_driver_path = "D:\Codigo\Pthon\ChromeDriver\chromedriver.exe"

        options = Options()
        options.binary_location = 'C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe'
        self.driver = webdriver.Chrome(options=options, executable_path=chrome_driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        cookies_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        cookies_button.click()

        time.sleep(2)

        start_button = self.driver.find_element_by_class_name("start-text")
        start_button.click()

        time.sleep(90)
        try:
            down_speed = self.driver.find_element_by_class_name("download-speed").text
            self.down = float(down_speed)

            up_speed = self.driver.find_element_by_class_name("upload-speed").text
            self.up = float(up_speed)
            print(self.down)
            print(self.up)

        except:
            self.driver.quit()
            print("There was not enough time to finish the test")
        else:
            if self.down < 500:
                self.tweet_at_provider()
            else:
                self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        email = self.driver.find_element_by_name("session[username_or_email]")
        email.send_keys(EMAIL)

        password = self.driver.find_element_by_name("session[password]")
        password.send_keys(PASSWORD)

        login = self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span")
        login.click()

        time.sleep(5)

        tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/span')
        tweet.send_keys(f"Hey internet provider, why is my internet speed {self.down}down/{self.up}up when I pay for 50/50")

        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()