from time import sleep, time
from random import randint, uniform, choice, shuffle

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from data.config import config


class CheckProfileOpenStatusException(Exception):
    pass


class OpenProfileException(Exception):
    pass


class CloseProfileException(Exception):
    pass


class AlreadyFollowingException(Exception):
    pass


class AdsPowerProfile:
    API_ROOT = 'http://local.adspower.com:50325'

    def __init__(self, name: str, _id: str, twitter_handle: str):
        self.name = name
        self._id = _id
        self.twitter_handle = twitter_handle
        self.profile_was_running = False
        self.driver = None
        self.action = None

    @staticmethod
    def random_sleep():
        sleep(randint(config["min_random_pause_sec"], config["max_random_pause_sec"]))

    def human_hover(self, element, click=False):
        size = element.size

        width_deviation_pixels = randint(1, int(size["width"] * config["max_width_deviation"]))
        height_deviation_pixels = randint(1, int(size["height"] * config["max_height_deviation"]))

        positive_width_deviation = randint(0, 1)
        positive_height_deviation = randint(0, 1)

        x = width_deviation_pixels if positive_width_deviation else -width_deviation_pixels
        y = height_deviation_pixels if positive_height_deviation else -height_deviation_pixels

        if click:
            self.action.move_to_element_with_offset(element, x, y).click().perform()
        else:
            self.action.move_to_element_with_offset(element, x, y).perform()

    def human_type(self, text: str):
        for char in text:
            sleep(uniform(config["min_typing_pause_seconds"], config["max_typing_pause_seconds"]))
            self.driver.switch_to.active_element.send_keys(char)

    def init_webdriver(self, driver_path: str, debug_address: str):
        chrome_driver = driver_path
        chrome_options = Options()
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "eager"

        chrome_options.add_experimental_option("debuggerAddress", debug_address)
        driver = webdriver.Chrome(chrome_driver, options=chrome_options, desired_capabilities=caps)
        self.driver = driver
        self.action = ActionChains(driver)

    def is_profile_open(self) -> bool:
        url = self.API_ROOT + '/api/v1/browser/active'
        params = {
            "user_id": self._id,
        }

        response = requests.get(url, params=params).json()
        if response["code"] != 0:
            raise CheckProfileOpenStatusException('Failed to check profile open status')

        if response['data']['status'] == 'Active':
            self.init_webdriver(response["data"]["webdriver"], response["data"]["ws"]["selenium"])
            return True
        if response['data']['status'] == 'Inactive':
            return False

    def open_profile(self, headless: bool = False):
        if self.is_profile_open():
            self.profile_was_running = True
            return

        url = self.API_ROOT + '/api/v1/browser/start'
        params = {
            "user_id": self._id,
            "open_tabs": "0",
            "ip_tab": "0",
            "headless": "1" if headless else "0",
        }

        response = requests.get(url, params=params).json()
        if response["code"] != 0:
            raise OpenProfileException('Failed to open profile')

        self.init_webdriver(response["data"]["webdriver"], response["data"]["ws"]["selenium"])

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
        self.dodge_modals()
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, '[href="/compose/tweet"]')
        try:
            self.human_hover(tweet_button, click=True)
        except:
            tweet_button.click()

        self.random_sleep()
        self.dodge_modals()
        self.human_type(tweet_text + ' ')

        self.random_sleep()
        self.dodge_modals()
        final_tweet_button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButton"]')
        try:
            self.human_hover(final_tweet_button, click=True)
        except:
            final_tweet_button.click()

        self.random_sleep()
        self.dodge_modals()

    def subscribe(self, username: str):
        self.driver.implicitly_wait(30)
        self.driver.get(f'https://twitter.com/{username}')

        self.random_sleep()
        self.dodge_modals()
        try:
            follow_button = self.driver.find_element(By.CSS_SELECTOR, f'[aria-label="Follow @{username}"]')
        except NoSuchElementException:
            self.driver.find_element(By.CSS_SELECTOR, f'[aria-label="Following @{username}"]')
            raise AlreadyFollowingException()

        try:
            self.human_hover(follow_button, click=True)
        except:
            follow_button.click()

        self.random_sleep()
        self.dodge_modals()

    def dodge_modals(self):
        self.driver.implicitly_wait(5)

        try:
            modal = self.driver.find_element(By.CSS_SELECTOR, f'[data-testid="sheetDialog"]')
            buttons = modal.find_elements(By.CSS_SELECTOR, f'[data-testid="sheetDialog"] div[role="button"]')

            for button in buttons:
                if button.text in config['modals_buttons_to_press']:
                    self.random_sleep()
                    try:
                        self.human_hover(button, click=True)
                    except:
                        button.click()
                    finally:
                        return
        except:
            pass

    def scroll_feed_with_shortcuts(self):
        for i in range(randint(config['min_feed_scrolls_per_episode'], config['max_feed_scrolls_per_episode'])):
            self.action.send_keys('j').perform()
            sleep(uniform(config['min_feed_scrolls_delay_sec'], config['max_feed_scrolls_delay_sec']))

    def surf_feed(self):
        def like_feed_tweet(_active_element):
            like_button = _active_element.find_element(By.CSS_SELECTOR, '[data-testid="like"]')
            try:
                self.human_hover(like_button, click=True)
            except:
                like_button.click()

        def retweet_feed_tweet(_active_element):
            retweet_button = _active_element.find_element(By.CSS_SELECTOR, '[data-testid="retweet"]')
            try:
                self.human_hover(retweet_button, click=True)
            except:
                retweet_button.click()

            self.random_sleep()
            retweet_confirm_button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="retweetConfirm"]')
            try:
                self.human_hover(retweet_confirm_button, click=True)
            except:
                retweet_confirm_button.click()

        def subscribe_feed_account(_active_element):
            user_profile = _active_element.find_element(By.CSS_SELECTOR, '[data-testid="Tweet-User-Avatar"]')
            self.human_hover(user_profile, click=False)
            self.random_sleep()
            hover_card = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="HoverCard"]')

            try:
                hover_card.find_element(By.XPATH, '//div[contains(@data-testid, "-unfollow")]')
                return
            except:
                try:
                    follow_button = hover_card.find_element(By.XPATH, '//div[contains(@data-testid, "-follow")]')
                except:
                    return
            try:
                self.human_hover(follow_button, click=True)
            except:
                follow_button.click()

        self.driver.implicitly_wait(30)
        self.driver.get('https://twitter.com/home')

        self.random_sleep()
        self.dodge_modals()

        for i in range(randint(config['min_feed_scroll_episodes'], config['max_feed_scroll_episodes'])):
            self.random_sleep()
            self.dodge_modals()
            self.scroll_feed_with_shortcuts()
            self.random_sleep()

            to_subscribe = True if (uniform(0, 1) <= config['feed_subscribe_probability']) else False
            to_retweet = True if (uniform(0, 1) <= config['feed_retweet_probability']) else False
            to_like = True if (uniform(0, 1) <= config['feed_like_probability']) else False

            if not to_subscribe + to_retweet + to_like:
                continue

            all_tweet_interactions = []
            if to_subscribe:
                all_tweet_interactions.append(subscribe_feed_account)
            if to_retweet:
                all_tweet_interactions.append(retweet_feed_tweet)
            if to_like:
                all_tweet_interactions.append(like_feed_tweet)
            shuffle(all_tweet_interactions)

            active_element = self.driver.execute_script("return document.activeElement")
            for interaction in all_tweet_interactions:
                try:
                    interaction(active_element)
                except Exception as e:
                    break
                finally:
                    self.random_sleep()
                    self.dodge_modals()
