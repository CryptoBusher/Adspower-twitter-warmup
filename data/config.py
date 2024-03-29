config = {
    # запускать браузер в скрытом режиме (True / False)
    "headless": True,

    # настройки сценария прогрева
    "post_tweet": True,  # делать ли рандомный твит (True / False)
    "surf_feed": True,  # делать ли серфинг по ленте
    "min_random_users_to_follow": 2,  # сколько минимум рандомных юзеров зафолловить (0, если иногда можно ни на кого не подписываться)
    "max_random_users_to_follow": 5,  # сколько максимум рандомных юзеров зафолловить (0, если не нужно подписываться вообще)
    "mandatory_users_to_follow": ['doliacat', 'binance'], # на кого обязательно подписываться ([], если не нужно)

    # сколько профилей прогреть
    "profiles_to_warmup": 10,

    # пауза между аккаунтами в минутах
    "min_idle_minutes": 10,
    "max_idle_minutes": 30,

    # пауза перед следующим действием в рамках прогрева
    "min_random_pause_sec": 4,
    "max_random_pause_sec": 15,

    # пауза между вводом символов в процессе печатания
    "min_typing_pause_seconds": 0.02,
    "max_typing_pause_seconds": 0.8,

    # селениум кликает всегда в один и тот же пиксель, этот параметр отвечает
    # за максимальное рандомное отклонение от этого пикселя (0 - 1)
    "max_height_deviation": 0.1,
    "max_widht_deviation": 0.1,

    # работать с уже открытыми профилями (позволяет параллельно прогреву работать
    # над своими задачами без вмешательства в них скрипта
    "warmup_running_profiles": False,

    "min_feed_scroll_episodes": 3,  # минимальное количество эпизодов прокрута ленты
    "max_feed_scroll_episodes": 6,  # максимальное количество эпизодов прокрута ленты
    "min_feed_scrolls_per_episode": 5,  # сколько минимум твитов прокрутить в пределах эпизода
    "max_feed_scrolls_per_episode": 10,  # сколько максимум твитов прокрутить в пределах эпизода
    "min_feed_scrolls_delay_sec": 0.1,  # минимальная задержка между прокрутами в рамках эпизода
    "max_feed_scrolls_delay_sec": 1,  # максимальная задержка между прокрутами в рамках эпизода

    "feed_subscribe_probability": 1,
    # вероятность того что аккаунт подпишется на автора поста в пределах эпизода (0 - 1)
    "feed_retweet_probability": 1,  # вероятность того что аккаунт ретвитнет пост в пределах эпизода (0 - 1)
    "feed_like_probability": 1,  # вероятность того что аккаунт лайкнет пост в пределах эпизода (0 - 1)

    # текст кнопок, которые надо нажать в случае появления всплывающих модальных окон
    "modals_buttons_to_press": [
        "Yes, that's correct"
    ]
}
