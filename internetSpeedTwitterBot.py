from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

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

        time.sleep(120)
        try:
            down_speed = self.driver.find_element_by_class_name("download-speed").text
            self.down = float(down_speed)

            up_speed = self.driver.find_element_by_class_name("upload-speed").text
            self.up = float(up_speed)
            print(self.down)
            print(self.up)

        except:
            print("There was not enough time to finish the test")
        finally:
            self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get()

        log_in = self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div/main/div/div/div[1]/div[1]/div/div[3]/div[4]/span/span")
        log_in.click()

        google_log_in = self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/div/div/div/main/div/div/div[1]/div[1]/div/div[3]/div[1]/div/span/span")
        google_log_in.click()

        time.sleep(2)

        self.driver.switch_to.window(self.driver.window_handles[1])

        email = self.driver.find_element_by_id("identifierId")
        email.send_keys()

