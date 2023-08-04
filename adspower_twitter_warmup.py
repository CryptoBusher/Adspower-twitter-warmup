from random import choice, randint, shuffle
from sys import stderr
from time import sleep

from loguru import logger
from pyfiglet import Figlet

from src.Profile import AdsPowerProfile, AlreadyFollowingException
from data.config import config
from data.profile_ids import profile_ids

logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <white>{message}</white>")

f = Figlet(font='5lineoblique')
print(f.renderText('Busher'),
      'Telegram channel: @CryptoKiddiesClub',
      'Telegram chat: @CryptoKiddiesChat',
      'Twitter: @CryptoBusher', sep='\n', end='\n\n')


def start_warmup(_profile: AdsPowerProfile):
    def mandatory_follow():
        if len(config['mandatory_users_to_follow']):
            logger.info(f'{_profile.name} - following mandatory {len(config["mandatory_users_to_follow"])} accounts')
            for user in config['mandatory_users_to_follow']:
                try:
                    _profile.subscribe(user)
                except AlreadyFollowingException:
                    logger.info(f'{_profile.name} - already following user @{user}')
                except Exception as err:
                    logger.error(f'{_profile.name} - failed to follow user @{user},')

    def random_follow():
        if config['max_random_users_to_follow']:
            users_to_follow_amount = randint(config['min_random_users_to_follow'], config['max_random_users_to_follow'])
            logger.info(f'{_profile.name} - following random {users_to_follow_amount} accounts')
            for i in range(users_to_follow_amount):
                user = choice(random_users_to_follow)
                try:
                    _profile.subscribe(user)
                except AlreadyFollowingException:
                    logger.info(f'{_profile.name} - already following user @{user}')
                except Exception as err:
                    logger.error(f'{_profile.name} - failed to follow user @{user}')

    def post_tweet():
        if config['post_tweet']:
            logger.info(f'{_profile.name} - posting tweet')
            try:
                tweet_text = choice(tweets)
                _profile.post_tweet(tweet_text)
                logger.info(f'{_profile.name} - tweet posted')
            except Exception as err:
                logger.error(f'{_profile.name} - failed to post tweet')
            finally:
                sleep(5)
                _profile.driver.get_screenshot_as_file(f"data/screenshots/{_profile.name}_posted_tweet.png")

    def surf_feed():
        if config['surf_feed']:
            logger.info(f'{_profile.name} - surfing feed')
            try:
                profile.surf_feed()
                logger.info(f'{_profile.name} - finished surfing feed')
            except Exception as err:
                logger.error(f'{_profile.name} - failed to surf feed: {err}')

    # open profile
    logger.info(f'{_profile.name} - starting warmup')
    try:
        _profile.open_profile(config["headless"])
        if _profile.profile_was_running:
            logger.info(f'{_profile.name} - profile was already running')
            if not config['warmup_running_profiles']:
                return
        _profile.driver.maximize_window()
    except Exception as _e:
        logger.error(f'{_profile.name} - failed to open profile, reason: {_e}')
        return

    # warmup
    all_actions = [
        mandatory_follow,
        random_follow,
        post_tweet,
        surf_feed
    ]
    shuffle(all_actions)

    for action in all_actions:
        action()

    # close profile
    if not _profile.profile_was_running:
        logger.info(f'{_profile.name} - closing profile')
        try:
            _profile.close_profile()
        except Exception as _e:
            logger.error(f'{_profile.name} - failed to close profile, reason: {_e}')


if __name__ == "__main__":
    with open('data/twitter_handles.txt', 'r') as file:
        twitter_handles = [i.strip() for i in file]

    with open('data/random_users_to_follow.txt', 'r') as file:
        random_users_to_follow = [i.strip() for i in file]

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
