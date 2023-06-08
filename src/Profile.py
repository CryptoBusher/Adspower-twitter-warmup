from time import sleep
from random import randint, uniform

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from data.config import config


class OpenProfileException(Exception):
    pass


class CloseProfileException(Exception):
    pass


class AdsPowerProfile:
    API_ROOT = 'http://local.adspower.com:50325'

    def __init__(self, name: str, _id: str, twitter_handle: str):
        self.name = name
        self._id = _id
        self.twitter_handle = twitter_handle
        self.driver = None

    @staticmethod
    def random_sleep():
        sleep(randint(config["min_random_pause_sec"], config["max_random_pause_sec"]))

    def human_click(self, click_object):
        size = click_object.size

        widht_deviation_pixels = randint(1, int(size["width"] * config["max_widht_deviation"]))
        height_deviation_pixels = randint(1, int(size["height"] * config["max_height_deviation"]))

        positive_width_deviation = randint(0, 1)
        positive_height_deviation = randint(0, 1)

        x = widht_deviation_pixels if positive_width_deviation else -widht_deviation_pixels
        y = height_deviation_pixels if positive_height_deviation else -height_deviation_pixels

        action = ActionChains(self.driver)
        action.move_to_element_with_offset(click_object, x, y).click().perform()

    def human_type(self, text: str):
        for char in text:
            sleep(uniform(config["min_typing_pause_seconds"], config["max_typing_pause_seconds"]))
            self.driver.switch_to.active_element.send_keys(char)

    def open_profile(self, headless: bool):
        url = self.API_ROOT + '/api/v1/browser/start'
        params = {
            "user_id": self._id,
            "open_tabs": "1",
            "ip_tab": "0",
            "headless": "1" if headless else "0",
        }

        response = requests.get(url, params=params).json()
        if response["code"] != 0:
            raise OpenProfileException('Failed to open profile')

        chrome_driver = response["data"]["webdriver"]
        chrome_options = Options()
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "eager"

        chrome_options.add_experimental_option("debuggerAddress", response["data"]["ws"]["selenium"])
        driver = webdriver.Chrome(chrome_driver, options=chrome_options, desired_capabilities=caps)
        self.driver = driver

    def close_profile(self):
        url_check_status = self.API_ROOT + '/api/v1/browser/active' + f'?user_id={self._id}'
        url_close_profile = self.API_ROOT + '/api/v1/browser/stop' + f'?user_id={self._id}'

        status = requests.get(url_check_status).json()
        if status['data']['status'] == 'Inactive':
            self.driver = None
            return

        response = requests.get(url_close_profile).json()
        if response["code"] != 0:
            raise CloseProfileException('Failed to close profile')

        self.driver = None

    def post_tweet(self, tweet_text: str):
        self.driver.implicitly_wait(30)

        self.driver.get(f'https://twitter.com/{self.twitter_handle}')

        self.random_sleep()
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, '[href="/compose/tweet"]')

        try:
            self.human_click(tweet_button)
        except:
            tweet_button.click()

        self.random_sleep()
        self.human_type(tweet_text)

        self.random_sleep()
        final_tweet_button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButton"]')

        try:
            self.human_click(final_tweet_button)
        except:
            final_tweet_button.click()
