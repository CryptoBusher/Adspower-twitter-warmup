from random import choice, randint
from sys import stderr
from time import sleep

from loguru import logger

from src.Profile import AdsPowerProfile
from data.config import config
from data.profile_ids import profile_ids


logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <white>{message}</white>")


def start_warmup(_profile: AdsPowerProfile):
    logger.info(f'{_profile.name} - starting warmup')
    try:
        _profile.open_profile(config["headless"])
        _profile.driver.maximize_window()
    except Exception as _e:
        logger.error(f'{_profile.name} - failed to open profile, reason: {_e}')
        return

    logger.info(f'{_profile.name} - posting tweet')
    try:
        tweet_text = choice(tweets)
        _profile.post_tweet(tweet_text)
        logger.info(f'{_profile.name} - tweet posted')
    except Exception as _e:
        logger.error(f'{_profile.name} - failed to post tweet, reason: {_e}')
    finally:
        sleep(5)
        _profile.driver.get_screenshot_as_file(f"data/screenshots/{_profile.name}_posted_tweet.png")

    logger.info(f'{_profile.name} - closing profile')
    try:
        _profile.close_profile()
    except Exception as _e:
        logger.error(f'{_profile.name} - failed to close profile, reason: {_e}')


if __name__ == "__main__":
    with open('data/twitter_handles.txt', 'r') as file:
        twitter_handles = [i.strip() for i in file]

    with open('data/tweets.txt', 'r', encoding="utf8") as file:
        tweets = [i.strip() for i in file]

    profiles = []
    for i, (profile_number, profile_id) in enumerate(profile_ids.items()):
        profiles.append(AdsPowerProfile(profile_number, profile_id, twitter_handles[i]))

    if config["profiles_to_warmup"] > len(profiles):
        logger.error(f"Amount of profiles to warmup > total amount of profiles, adjusted")
        config["profiles_to_warmup"] = len(profiles)

    for i in range(config["profiles_to_warmup"]):
        profile = profiles.pop(randint(0, len(profiles) - 1))
        start_warmup(profile)

        sleep_time = randint(config["min_idle_minutes"] * 60, config["max_idle_minutes"] * 60)
        logger.info(f'Sleeping {round(sleep_time / 60, 1)} minutes')
        sleep(sleep_time)
